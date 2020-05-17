# Core
from fsociety.core.menu import tools_cli

from .cupp import cupp

__tools__ = {
    "cupp": cupp
}


def cli():
    tools_cli(__name__, __tools__)
