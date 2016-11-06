# map reduce practice

from functools import reduce


def up_case(s):
    return s[0].upper() + s[1:].lower()


L = ["ABC", "abc", "hjk"]
print(list(map(up_case, L)))


def add_(x, y):
    return x + y


L = [1, 2, 3, 4, 5]
print(reduce(add_, L))


def str2int(s):
    def f(x, y):
        return x * 10 + y

    def char2int(c):
        return {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}[c]

    return reduce(f, map(char2int, s))


def str2float(s):
    def char2int(c):
        return {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0, '.': '.'}[c]

    return reduce(lambda x, y: x * 10 + y, map(char2int, s))


# print(str2int('798247'))


def prod(l):
    return str(reduce(lambda x, y: x * y, l))


print('1*2*3*4=' + prod([1, 2, 3, 4]))
