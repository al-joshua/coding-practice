#!/usr/bin/env python

"""
The script will:
- receive exectly one argument a coma separated list of positive integers
- will pack the number of reservations if there are at least 2 adjacent reservations  with the same hotel id in the
following format:
    <hotel_id>:<number_of_ocurrences>
- scipt has to be executable file

eg:
$ ./bookingcom\ task\ 2.py 2234,2234,765345,22,31234,31234,99756,189,189,189,31234,22
2234:2,765345,22,31234:2,99756,189:4,31234,22:1
"""

import sys


def counts(data):
    dct = {}
    for id in set(data):
        c = data.count(id)
        if str(c) in dct.keys():
            dct[str(c)].append(id)
        else:
           dct.update({str(c): [id]})
    return dct


def formatter(arg):
    res = []
    d = counts(arg)
    for k in d:
        s = '{}:{}'.format(','.join(d[k]), k)
        res.append(s)
    return ','.join(res)


def main():
    input = sys.argv[1].split(',')
    print(formatter(input))


if __name__ == '__main__':
    main()