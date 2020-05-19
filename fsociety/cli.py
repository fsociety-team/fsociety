#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse

import colorama
from colorama import Fore, Back, Style

# Core
from fsociety.core.menu import set_readline, format_menu_item, format_tools, module_name, prompt, clear_screen
from fsociety.core.config import get_config, write_config
from fsociety.core.builtins import print_contributors, spawn_shell

# Modules
import fsociety.information_gathering
import fsociety.passwords
import fsociety.web_apps
import fsociety.obfuscation

# Config
config = get_config()

# Menu
TERMS = Fore.YELLOW + """
I shall not use fsociety to:
(i) upload or otherwise transmit, display or distribute any
content that infringes any trademark, trade secret, copyright
or other proprietary or intellectual property rights of any
person; (ii) upload or otherwise transmit any material that contains
software viruses or any other computer code, files or programs
designed to interrupt, destroy or limit the functionality of any
computer software or hardware or telecommunications equipment;
""" + Fore.RESET
MENU_TITLE = Fore.RED + """
888888 .dP"Y8  dP"Yb   dP""b8 88 888888 888888 Yb  dP
88__   `Ybo." dP   Yb dP   `" 88 88__     88    YbdP
88""   o.`Y8b Yb   dP Yb      88 88""     88     8P
88     8bodP'  YbodP   YboodP 88 888888   88    dP

""" + Fore.RESET
MENU_ITEMS = [fsociety.information_gathering,
              fsociety.passwords, fsociety.web_apps, fsociety.obfuscation]
BUILTIN_FUNCTIONS = {
    "shell": spawn_shell,
    "devs": print_contributors,
    "exit": lambda: exec('raise KeyboardInterrupt'),
}
items = dict()


def menuitems():
    items_str = str()
    for value in MENU_ITEMS:
        name = module_name(value)
        tools = format_tools(value.__tools__)
        items_str += f"{format_menu_item(name)} {tools}\n\n"
    for key in BUILTIN_FUNCTIONS.keys():
        items_str += f"{format_menu_item(key)}\n\n"
    return items_str


def agreement():
    while not config.getboolean("fsociety", "agreement"):
        clear_screen()
        print(TERMS)
        agree = input(
            "You must agree to our terms and conditions first (Y/n) ")
        if agree.lower()[0] == "y":
            config.set('fsociety', 'agreement', 'true')


for item in MENU_ITEMS:
    items[module_name(item)] = item

commands = list(items.keys()) + list(BUILTIN_FUNCTIONS.keys())


def mainloop():
    agreement()
    print(MENU_TITLE)
    print(menuitems())
    selected_command = input(prompt()).strip()
    if not selected_command or (not selected_command in commands):
        print(f"{Fore.YELLOW}Invalid Command{Fore.RESET}")
        return
    if selected_command in BUILTIN_FUNCTIONS.keys():
        func = BUILTIN_FUNCTIONS.get(selected_command)
        return func()
    print(Style.RESET_ALL)
    try:
        func = items[selected_command].cli
        func()
    except Exception as e:
        print(str(e))


def interactive():
    colorama.init()
    try:
        while True:
            set_readline(commands)
            mainloop()
    except KeyboardInterrupt:
        print("\nExitting...")
        write_config(config)
        exit(0)


def main():
    parser = argparse.ArgumentParser(
        description='A Penetration Testing Framework')
    parser.add_argument('-w', '--web', action='store_true',
                        help='start web ui')
    parser.add_argument('-i', '--interactive',
                        action='store_true', help='start interaction cli')
    parser.add_argument('-t', '--tool', help='run tool')

    args = parser.parse_args()

    if args.interactive:
        interactive()
    elif args.tool:
        print("TODO: Run tool by name")
    elif args.web:
        print("TODO: Webserver Here")
    else:
        interactive()


if __name__ == "__main__":
    main()
