# Core
from fsociety.core.menu import tools_cli

from .xsstrike import xsstrike

__tools__ = {
    "xsstrike": xsstrike
}


def cli():
    tools_cli(__name__, __tools__)
