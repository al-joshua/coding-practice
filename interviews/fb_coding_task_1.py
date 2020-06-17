'''
create a function which takes array a, starting index i and ending index j. Return array where elements
 from i to j are reversed.

eg: a = ('a', 'b', 'c', 'd', 'e', 'f' , 'g')
i = 2
j = 5

returning array will be  ['a', 'b', 'f', 'e', 'd', 'c', 'g']
'''


def funct_opt1(a, i, j):
    l = []
    for index in range(len(a)):
        if index in range(i,j+1):
            l.append(a[i - index -2])
        else: l.append(a[index])
    return l


def funct_opt2(a, i, j):
    return ','.join(''.join(a[:i]) + ''.join(reversed(a[i:j+1])) + ''.join(a[j+1:])).split(',')


def funct_opt3(a, i, j):
    a = list(a)
    for k in range(j - i - 1):
        a[i + k], a[j - k] = a[j - k], a[i + k]

    return a

