import argparse
import builtins
import os
import readline

from myth_parse import parser

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v',
        '--verbose',
        help='Show debugging output',
        action='store_true'
    )
    return parser.parse_args()

def main():
    args = parse_args()
    builtins.verbose = args.verbose

    historypath = os.path.expanduser('~/.mythhistory')

    if not os.path.exists(historypath):
        open(historypath, 'a').close()

    readline.read_history_file(historypath)

    while True:
        try:
            s = input('myth> ')
            if s:
                readline.append_history_file(1, historypath)
                parser.parse(s)
        except EOFError:
            break
        except Exception as e:
            print(e)
            print()

if __name__ == '__main__':
    main()