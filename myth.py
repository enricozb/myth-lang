import argparse
import builtins
import os
import readline

from myth_parse import parser

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',
        nargs='?',
        default=None,
        help='Name of file to run',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        type=int,
        help='Verboseness level',
        default=0
    )
    return parser.parse_args()

def main():
    args = parse_args()
    builtins.verbose = args.verbose
    if builtins.verbose:
        print(f'Verbose mode {builtins.verbose} enabled')

    if args.filename:
        with open(args.filename, 'r') as file:
            for line in file:
                parser.parse(line)
        return

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
            if builtins.verbose > 1:
                raise e
            print(e)
            print()

if __name__ == '__main__':
    main()