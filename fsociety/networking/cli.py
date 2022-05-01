# Core
from fsociety.core.menu import tools_cli

from .bettercap import bettercap
from .nmap import nmap

__tools__ = [nmap, bettercap]


def cli():
    tools_cli(__name__, __tools__)
