#!/usr/bin/env python

import os
import sys
import re


def dir_parser(path):
    result = []
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_symlink():
                result.append(os.readlink(os.path.join(path, entry.name)))
            elif entry.is_file():
                result.append(entry.name)
    return result


def ext_regexer(item):
    regex = re.search('\.\D+$',item)
    return regex.group() if regex else None


def file_lister(path):
    string = []
    for file in sorted(set(dir_parser(path))):
        if ext_regexer(file):
            file = file.strip(ext_regexer(file))
        string.append(file)
    return '\n'.join(string)


def main():
    try:
        path = sys.argv[1]
    except IndexError:
        print('ERROR: you need specify a directory')
    else:
        if os.path.isfile(path) or not os.path.isdir(path):
            print('ERROR: argument specified is not valid')
        else:
            print(file_lister(path))


if __name__ == '__main__':
    main()