import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline
from fsociety.core.usernames import get_usernames, add_username


class sherlockRepo(GitHubRepo):
    def __init__(self, path="sherlock-project/sherlock", install={"pip": "requirements.txt"}):
        super().__init__(path=path, install=install)

    def run(self):
        os.chdir(self.full_path)
        usernames = get_usernames()
        set_readline(usernames)
        inputted_usernames = input("\nEnter one or more usernames: ").strip()
        for username in inputted_usernames.split():
            if not username in usernames:
                add_username(username)
        return os.system(f"python3 sherlock {inputted_usernames} -r")


sherlock = sherlockRepo()
