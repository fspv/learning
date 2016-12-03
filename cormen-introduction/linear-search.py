from random import randint

x = sorted([ randint(0, 100) for i in xrange(0, 100) ])
search = 32


def linear_search(x, search):
    i = 0
    while i < len(x):
        if x[i] == search:
            return i
        i += 1
    return -1


def linear_search_optimized(x, search):
    i = 0
    last = x[len(x) - 1]
    x[len(x) - 1] = search
    while x[i] != search:
        i += 1
    if i == (len(x) - 1):
        if last == search:
            return i
        else:
            return -1
    else:
        return i


print linear_search(x, search)
print linear_search_optimized(x, search)
