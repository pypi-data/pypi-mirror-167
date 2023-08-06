#!/usr/bin/env python

import argparse
import importlib
import sys


def globals(imports):
    g = {}

    for stmt in imports.split(","):
        name, _, alias = map(lambda s: s.strip(),
                             stmt.strip().partition(' as '))
        alias = alias or name
        g[alias] = importlib.import_module(name)

    return g


def locals(replace_str, line):
    return {replace_str: line}


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--imports', default='json as j, base64 as b64, re',
                        help="Imports in python syntax, e.g.: 'requests as r, re, ...'.")
    parser.add_argument('-v', '--item-var', default='I',
                        help="Name of the variable with the item passed to the script.")
    parser.add_argument('script', help="Script to invoke on each input line.")
    parser.add_argument('file', nargs='?', default='-',
                        help="Input file. Use '-' for STDIN.")
    args = parser.parse_args()

    input_file = sys.stdin if args.file == "-" else open(args.file)
    g = globals(args.imports)

    for line in input_file:
        line = line.rstrip('\r\n')
        if not line:
            continue

        l = locals(args.item_var, line)
        eval(args.script, g, l)


if __name__ == '__main__':
    main()
