# pylint: disable=unused-import,broad-except,inconsistent-return-statements
import os
import shutil
from typing import Iterable

from rich.text import Text
from rich.table import Table
from rich.style import Style
from rich import box

from fsociety.console import console
from fsociety.core.config import INSTALL_DIR

BACK_COMMANDS = ["back", "return"]


class CommandCompleter:
    def __init__(self, options: Iterable[str]):
        self.options = sorted(options)

    def complete(self, text: str, state: int):
        response = None
        matches = []
        if state == 0:
            if text:
                matches = [s for s in self.options if s and s.startswith(text.lower())]
            else:
                matches = self.options[:]
        try:
            response = matches[state]
        except IndexError:
            pass
        return response


def set_readline(items: Iterable[str]):
    try:
        import readline
    except ImportError:
        pass
    else:
        import rlcompleter  # noqa: F401

        if isinstance(items, list):
            readline.set_completer(CommandCompleter(items).complete)
        elif isinstance(items, dict):
            readline.set_completer(CommandCompleter(items.keys()).complete)
        else:
            readline.set_completer(CommandCompleter(list(items)).complete)
        readline.parse_and_bind("tab: complete")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def format_tools(tools):
    cutoff = 5
    etc = False
    if len(tools) > cutoff:
        tools = tools[:cutoff]
        etc = True
    res = "".join([f"\n{str(tool)}" for tool in tools])
    if etc:
        res += "\n..."
    return res


def module_name(module):
    return module.__name__.split(".")[-1]


def prompt(path="", base_path="~"):
    encoded_path = os.path.join(base_path, path, "")
    return f"\nfsociety {encoded_path}# "


def input_wait():
    input("\nPress [ENTER] to continue... ")


def tools_cli(name, tools, links=True):
    table = Table(box=box.HEAVY_HEAD)
    table.add_column("Name", style="red", no_wrap=True)
    table.add_column("Description", style="magenta")
    if links:
        table.add_column("Link", no_wrap=True)

    tools_dict = dict()
    for tool in tools:
        tools_dict[str(tool)] = tool
        args = [str(tool), tool.description]
        if links:
            text_link = Text(f"{tool.path}")
            text_link.stylize(Style(link=f"https://github.com/{tool.path}"))
            args.append(text_link)
        table.add_row(*args)

    console.print(table)
    console.print("back", style="command")
    set_readline(list(tools_dict.keys()) + BACK_COMMANDS)
    selected_tool = input(prompt(name.split(".")[-2])).strip()
    if selected_tool not in tools_dict.keys():
        if selected_tool in BACK_COMMANDS:
            return
        console.print("Invalid Command", style="bold yellow")
        return tools_cli(name, tools, links)
    tool = tools_dict.get(selected_tool)
    if hasattr(tool, "install") and not tool.installed():
        tool.install()
    try:
        response = tool.run()
        if response and response > 0 and response != 256:
            console.print(
                f"{selected_tool} returned a non-zero exit code", style="bold red"
            )
            if hasattr(tool, "install") and confirm("Do you want to reinstall?"):
                os.chdir(INSTALL_DIR)
                shutil.rmtree(tool.full_path)
                tool.install()
    except KeyboardInterrupt:
        return

    return input_wait()


def confirm(message="Do you want to?"):
    response = input(f"{message} (y/n): ").lower()
    if response:
        return response[0] == "y"
    return False
