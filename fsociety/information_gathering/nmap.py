from fsociety.core.repo import GitHubRepo

install = {
    "default": "./configure && make && make install",
}


class nmapRepo(GitHubRepo):
    def __init__(self, path="nmap/nmap", install=install):
        super().__init__(path=path, install=install)

    def install(self):
        path = self.clone

    def run(self):
        print("Running nmap")


nmap = nmapRepo()
