import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline
from fsociety.core.usernames import get_usernames, add_username


class sherlockRepo(GitHubRepo):
    def __init__(self):
        super().__init__(path="sherlock-project/sherlock",
                         install={"pip": "requirements.txt"}, 
                         description="Hunt down social media accounts by username across social networks")

    def run(self):
        os.chdir(self.full_path)
        usernames = get_usernames()
        set_readline(usernames)
        user_usernames = input("\nEnter one or more usernames: ").strip()
        for username in user_usernames.split():
            if not username in usernames:
                add_username(username)
        return os.system(f"python3 sherlock {user_usernames} -r")


sherlock = sherlockRepo()
