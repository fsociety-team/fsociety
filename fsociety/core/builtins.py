import os
from requests import get

from colorama import Fore

from .menu import input_wait
from .config import install_dir


def print_contributors():
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


def spawn_shell():
    print("Enter `exit` to return to fsociety")
    shell = os.getenv("SHELL")
    os.chdir(install_dir)
    os.system(shell)
