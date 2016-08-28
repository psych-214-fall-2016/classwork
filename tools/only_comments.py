""" Strip all not-blank lines from a file that do not begin with #

Write to stdout
"""

import sys

def main():
    fname = sys.argv[1]
    with open(fname, 'rt') as fobj:
        for line in fobj:
            if line.strip().startswith('#') or line.strip() == '':
                sys.stdout.write(line)


if __name__ == '__main__':
    main()
