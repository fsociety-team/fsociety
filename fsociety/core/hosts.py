import os.path
from typing import List

from fsociety.core.config import INSTALL_DIR, get_config

config = get_config()

full_path = os.path.join(INSTALL_DIR, config.get("fsociety", "host_file"))


class InvalidHost(Exception):
    pass


def get_hosts() -> List[str]:
    try:
        with open(full_path, encoding="utf-8") as hostfile:
            return [host.strip() for host in hostfile]
    except FileNotFoundError:
        return []


def add_host(host: str) -> None:
    if not host:
        raise ValueError
    with open(full_path, "a", encoding="utf-8") as hostfile:
        hostfile.write(f"\n{host}")
