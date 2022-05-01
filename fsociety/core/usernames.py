import os.path
from typing import List

from fsociety.core.config import INSTALL_DIR, get_config

config = get_config()

full_path = os.path.join(INSTALL_DIR, config.get("fsociety", "usernames_file"))


def get_usernames() -> List[str]:
    try:
        with open(full_path) as usernamefile:
            return [username.strip() for username in usernamefile]
    except FileNotFoundError:
        return list()


def add_username(username: str) -> None:
    with open(full_path, "a") as usernamefile:
        usernamefile.write(f"\n{username}")
