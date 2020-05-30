import os.path

from fsociety.core.config import INSTALL_DIR, get_config

config = get_config()

full_path = os.path.join(INSTALL_DIR, config.get("fsociety", "host_file"))


class InvalidHost(Exception):
    pass


def get_hosts():
    try:
        with open(full_path, "r") as hostfile:
            return [host.strip() for host in hostfile]
    except FileNotFoundError:
        return list()


def add_host(host):
    if not host:
        raise ValueError
    with open(full_path, "a") as hostfile:
        hostfile.write(f"\n{host}")
