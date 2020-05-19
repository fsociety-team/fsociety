import os.path

from fsociety.core.config import install_dir, get_config

config = get_config()

full_path = os.path.join(install_dir, config.get("fsociety", "host_file"))


class InvalidHost(Exception):
    pass


def verify_host(host):
    print("TODO: Finish Function")


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
