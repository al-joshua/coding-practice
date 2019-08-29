#!/usr/bin/env python

import sys


def counts(data):
    dct = {}
    for id in set(data):
        c = data.count(id)
        if c >= 2:
            print(id,c)
            if str(c) in dct.keys():
                dct[str(c)].append(id)
            else:
                dct.update({str(c): [id]})
    return dct


def formatter():
    res = ''
    d = counts(sys.argv[1])
    for k in d:
        s = '{}:{},'.format(str(d[k]).strip('[]'), int(k))
        res += s
    return res


def main():
    print(formatter())


if __name__ == '__main__':
    main()