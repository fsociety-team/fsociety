import os

from fsociety.core.repo import GitHubRepo


class hashBusterRepo(GitHubRepo):
    def __init__(self):
        super().__init__(path="s0md3v/Hash-Buster",
                         install=None,
                         description="Why crack hashes when you can bust them?")

    def run(self):
        os.chdir(self.full_path)
        user_hash = input("\nEnter a hash: ").strip()
        return os.system(f"python3 hash.py -s {user_hash}")


hash_buster = hashBusterRepo()
