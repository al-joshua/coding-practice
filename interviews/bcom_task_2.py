#!/usr/bin/env python

"""
The script will:
- receive exectly one argument a coma separated list of positive integers
- will pack the number of reservations if there are at least 2 adjacent reservations  with the same hotel id in the
following format:
    <hotel_id>:<number_of_ocurrences>
- scipt has to be executable file

eg:
$ ./bcom_task_2.py 2234,2234,765345,22,31234,31234,99756,189,189,189,31234,22
2234,22:2,765345,99756:1,31234,189:3
"""

import sys


def counts(data):
    dct = {}
    for id in data:
        c = data.count(id)
        if c not in dct:
            dct.update({c: [id]})
        elif id not in dct[c]:
            dct[c].append(id)

    result = ','.join([','.join(map(str, v)) + ':' + str(k) for k, v in dct.items()])

    return result


def main():
    input = sys.argv[1].split(',')
    print(counts(input))


if __name__ == '__main__':
    main()