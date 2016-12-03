from random import randint

x = sorted([ randint(0, 100) for i in xrange(0, 100) ])
search = 32

print("x: {}".format(x))
print("search: {}".format(search))


def binary_search(x, search):
    found = -1
    p = 0
    r = len(x) - 1

    while found == -1 and r >= p:
        q = (p + r) / 2
        if x[q] == search:
            found = q
        if x[q] < search:
            p = q + 1
        elif x[q] > search:
            r = q - 1

    return found


def recursive_binary_search(x, search, p=0, r=(len(x) - 1)):
    q = (p + r) / 2
    if p > r:
        return -1
    if x[q] == search:
        return q
    elif x[q] < search:
        return recursive_binary_search(
            x, search,
            (q + 1), r,
        )
    elif x[q] > search:
        return recursive_binary_search(
            x, search,
            p, (q - 1),
        )


print binary_search(x, search)
print recursive_binary_search(x, search)

