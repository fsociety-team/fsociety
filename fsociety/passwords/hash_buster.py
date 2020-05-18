import os

from fsociety.core.repo import GitHubRepo


class hashBusterRepo(GitHubRepo):
    def __init__(self, path="s0md3v/Hash-Buster", install=None):
        super().__init__(path=path, install=install)

    def run(self):
        os.chdir(self.full_path)
        user_hash = input("\nEnter a hash: ").strip()
        return os.system(f"python3 hash.py -s {user_hash}")


hash_buster = hashBusterRepo()
