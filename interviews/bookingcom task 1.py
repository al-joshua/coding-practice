#!/usr/bin/env python

'''Count the number of duplicate ip addresses in file and print out 10 most frequent entries. Input file is 'logfile'.

eg:
31.184.238.87 132
14.140.27.2 121
122.163.225.169 76
54.216.161.184 65
122.162.143.20 47
125.21.240.2 37
122.163.131.243 36
121.241.120.70 35
1.39.101.60 34
125.21.198.150 33
'''


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
    res = process_data('logfile')
    for i in range(10):
        print('{} {}'.format(res[i][0], res[i][1]))


if __name__ == '__main__':
    main()