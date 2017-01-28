#!/usr/bin/env python2
from random import randint

x = [ randint(0, 1) for i in xrange(0, 100) ]

def really_simple_sort_py(x):
    out = []
    for i in xrange(len(x)):
        if x[i] == 0:
            out += [x[i]]

    for i in xrange(len(x) - len(out)):
        out += [1]

    return out

print really_simple_sort_py(x)
