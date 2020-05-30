# Core
from fsociety.core.menu import tools_cli

from .nmap import nmap
from .bettercap import bettercap

__tools__ = [str(tool) for tool in [nmap, bettercap]]


def cli():
    tools_cli(__name__, __tools__)
