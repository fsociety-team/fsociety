#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from .cli import cli

parser = argparse.ArgumentParser(description='A Penetration Testing Framework')
parser.add_argument('-w', '--web', action='store_true', help='start web ui')
parser.add_argument('-i', '--interactive',
                    action='store_true', help='start interaction cli')

args = parser.parse_args()

if args.interactive:
    cli()
elif args.web:
    print("TODO: Webserver Here")
else:
    parser.print_help()
