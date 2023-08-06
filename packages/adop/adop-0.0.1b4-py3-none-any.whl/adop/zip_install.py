import configparser
import json
import os
import pathlib

from . import __version__, auto_sequences, exceptions, parse_config


# TODO: Improve this
def compare_version(version: str, requires: str) -> bool:

    v1 = tuple(int(i) for i in version.split(".") if i.isdigit())
    v2 = tuple(int(i) for i in requires.split(".") if i.isdigit())
    return v1 >= v2


def install(file: str, config: str, cwd: str, remote: str):

    if cwd and not cwd == ".":
        os.chdir(os.path.expanduser(cwd))

    abs_conf_path = os.path.abspath(os.path.expanduser(config))
    local_config = parse_config.parse(abs_conf_path, "", "")

    installer = Installer(local_config)
    requires_data = installer.parse_requires(file)
    remote_data = installer.parse_remotes(remote)
    installer.install(remote_data, requires_data)


class Installer:
    def __init__(self, local_config: configparser.ConfigParser) -> None:
        self.config = local_config

    def parse_requires(self, requires_file: str) -> dict:
        requires_file_path = pathlib.Path.cwd().joinpath(requires_file)
        if not requires_file_path.exists():
            raise exceptions.CommandFail(
                f"Requires-file not found: {requires_file_path}"
            )
        requires = configparser.ConfigParser()
        requires.read_string(requires_file_path.read_text())

        if not requires.has_section("requires"):
            raise exceptions.CommandFail(
                f"Section [requires] is missing in file: {requires_file}"
            )

        if requires.has_option("tool_requires", "adop"):
            required_version = requires.get("tool_requires", "adop")
            if not compare_version(__version__, required_version):
                raise exceptions.CommandFail(
                    f"Required adop version {required_version} is not installed."
                )

        requires_data = {k: v for k, v in requires.items("requires")}
        return requires_data

    def parse_remotes(self, remote: str) -> dict:
        if not remote:
            remote = self.config.get("client", "remote")
        remote_section = f"remote:{remote}"

        if not self.config.has_section(f"remote:{remote}"):
            raise exceptions.CommandFail(
                f"Configuration error: section [remote:{remote}] not defined."
            )

        try:
            remote_data = {
                "url": self.config.get(remote_section, "url"),
                "token": self.config.get(remote_section, "token"),
                "insecure": self.config.getboolean(
                    remote_section, "insecure", fallback=False
                ),
            }
        except configparser.NoOptionError as err:
            raise exceptions.CommandFail(f"Configuration error: {err}")

        return remote_data

    def install(self, remote_data: dict, requires_data: dict):

        cache_root = self.config.get("client", "cache_root")
        install_root = self.config.get("client", "install_root")

        keep_on_disk = 0
        if self.config.getboolean("auto_delete", "on"):
            keep_on_disk = self.config.getint("auto_delete", "keep_on_disk")

        _handle_zip = auto_sequences.client_install_zip_sequence(
            install_root, cache_root, keep_on_disk, remote_data, requires_data
        )

        try:
            for res in _handle_zip:
                if isinstance(res, dict):
                    if "root" in res:
                        print(f"Requires: {res['root']}")
                    elif "result" in res:
                        print(f"{json.dumps(res)}")
                else:
                    print(f"          {res}")
        except exceptions.CommandFail as err:
            print("          ERROR:")
            raise exceptions.CommandFail(f"             {err}")
