# Core
from fsociety.core.menu import tools_cli

from .photon import photon
from .xsstrike import xsstrike

__tools__ = [xsstrike, photon]


def cli():
    tools_cli(__name__, __tools__)
