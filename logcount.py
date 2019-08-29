#!/usr/bin/env python


def func_sort(item):
    return item[1]


def process_data(file):
    res = []
    with open(file, 'r') as f:
        data = f.read()
    arr = data.splitlines()
    for ip in set(arr):
        count = arr.count(ip)
        res.append((ip,count))
    res.sort(key=func_sort, reverse=True)
    return res


def main():
    _ = process_data('logfile')
    for i in range(10):
        print('{} {}'.format(_[i][0], _[i][1]))


if __name__ == '__main__':
    main()