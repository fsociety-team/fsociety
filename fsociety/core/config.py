import os.path
from sys import platform
from pathlib import Path
from configparser import RawConfigParser, NoOptionError

from fsociety.__version__ import __version__

current_platform = platform
if platform in ["win32", "cygwin"]:
    current_platform = "windows"
elif platform.startswith("darwin"):
    current_platform = "macos"
elif platform.startswith("linux") or platform.startswith("freebsd"):
    current_platform = "linux"

install_dir = os.path.join(str(Path.home()), ".fsociety")
config_file = os.path.join(install_dir, "fsociety.cfg")

DEFAULT_CONFIG = {
    "version": __version__,
    "agreement": "false",
    "ssh_clone": "false",
    "os": current_platform,
    "host_file": "hosts.txt",
    "usernames_file": "usernames.txt"
}


def get_config():
    config = RawConfigParser()
    if not os.path.exists(install_dir):
        os.mkdir(install_dir)
    if not os.path.exists(config_file):
        config["fsociety"] = DEFAULT_CONFIG
        with open(config_file, "w") as configfile:
            config.write(configfile)
    config.read(config_file)
    check_config(config)
    config.set("fsociety", "version", __version__)
    return config


def write_config(config):
    with open(config_file, "w") as configfile:
        config.write(configfile)


def check_config(config):
    for key in DEFAULT_CONFIG.keys():
        try:
            config.get("fsociety", key)
        except NoOptionError:
            config.set("fsociety", key, DEFAULT_CONFIG.get(key))
    write_config(config)
