#!/usr/bin/env python2
from random import randint

m = 12
x = [ randint(0, 1) for i in xrange(0, 100) ]
print x
x_m = [ randint(0, m) for i in xrange(0, 100) ]
print x_m


def really_simple_sort(x):
    out = []
    for i in xrange(len(x)):
        if x[i] == 0:
            out += [x[i]]

    for i in xrange(len(x) - len(out)):
        out += [1]

    return out


def count_keys_equal(x, m):
    equal = [0] * (m + 1)
    for i in xrange(len(x)):
        equal[x[i]] = equal[x[i]] + 1

    return equal


def count_keys_less(equal):
    less = [0]
    for i in xrange(1, len(equal) + 1):
        less += [0]
        less[i] += less[i - 1] + equal[i - 1]

    return less


print really_simple_sort(x)
equal = count_keys_equal(x_m, m)
print count_keys_less(equal)
