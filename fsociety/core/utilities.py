import os
from requests import get
from socket import gethostbyname

from colorama import Fore

from .menu import input_wait, set_readline, tools_cli
from .config import install_dir
from .hosts import get_hosts, add_host
from .utility import Utility


class print_contributors(Utility):
    def run(self):
        print(Fore.RED + """
    8888b.  888888 Yb    dP .dP"Y8 
    8I  Yb 88__    Yb  dP  `Ybo." 
    8I  dY 88""     YbdP   o.`Y8b 
    8888Y"  888888    YP    8bodP'
    """)
        response = get(
            'https://api.github.com/repos/fsociety-team/fsociety/contributors')
        contributors = response.json()
        for contributor in sorted(contributors, key=lambda c: c['contributions'], reverse=True):
            username = contributor.get("login")
            print(f" {username} ".center(30, "-"))
        print(Fore.RESET)
        input_wait()


class spawn_shell(Utility):
    def run(self):
        print("Enter `exit` to return to fsociety")
        shell = os.getenv("SHELL")
        os.chdir(install_dir)
        os.system(shell)


class host2ip(Utility):
    def run(self):
        hosts = get_hosts()
        set_readline(hosts)
        user_host = input("\nEnter a host: ").strip()
        if not user_host in hosts:
            add_host(user_host)
        ip = gethostbyname(user_host)
        print(f"\n{user_host} has the IP of {ip}")


tools = [host2ip, spawn_shell, print_contributors]

__tools__ = dict()
for tool in tools:
    __tools__[tool.__name__] = tool


def cli():
    tools_cli(__name__, __tools__)
