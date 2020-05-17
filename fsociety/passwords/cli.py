# Core
from fsociety.core.menu import set_readline, format_tools

__tools__ = ["tool1", "tool2", "tool3"]


def cli():
    print("Passwords!")
    print(format_tools(__tools__))
    set_readline(__tools__)
    selected_tool = input("Select a tool: ")
    print(selected_tool)
