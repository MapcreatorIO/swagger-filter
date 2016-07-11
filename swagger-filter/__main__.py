#!/usr/bin/env python3
import yaml
import sys
from argparse import ArgumentParser, FileType


def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input',  metavar='FILE', type=FileType('r'),
                        default=sys.stdin, help='Input swagger.yml file')
    parser.add_argument('-o', '--output', metavar='FILE', type=FileType('w'),
                        default=sys.stdout, help='Output swagger.yml file')

    parser.add_argument('--remove-extensions', action='store_true', help='Remove all extensions')
    parser.add_argument('-e', '--exclude', action='append', help='Exclude all nodes containing x-? from output')
    args = parser.parse_args()

    exclude = list(map(lambda x: x.lower(), args.exclude or []))
    data = yaml.load(args.input)
    data = recurse_data(data, exclude, args.remove_extensions)
    yaml.dump(data, args.output)


def recurse_data(data, exclude, clean=False):
    keys = data.keys() if isinstance(data, dict) else range(len(data))
    keys = list(keys)

    offset = 0
    for key in keys:
        if isinstance(key, int):
            key = key - offset

        if isinstance(key, str) and key.lower()[2:] in exclude:# and data[key] is True and key.lower()[:2] == 'x-':
            sys.stderr.write('REMOVE HIT FOR {}\n'.format(key))
            return None

        if isinstance(key, str) and clean and key.lower()[:2] == 'x-':
            sys.stderr.write('CLEAN HIT FOR {}\n'.format(key))
            del data[key]
            continue

        if isinstance(data[key], dict) or isinstance(data[key], list):
            data[key] = recurse_data(data[key], exclude, clean)

            if data[key] is None:
                del data[key]
                offset += 1
                continue

    return data

if __name__ == '__main__':
    main()