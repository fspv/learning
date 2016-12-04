from random import randint

x = [ randint(0, 100) for i in xrange(0, 100) ]


def selection_sort(x):
    index_left_max = 0

    for i in xrange(len(x)):
        left_max = -1
        for j in xrange(i, len(x)):
            if x[j] > left_max:
                left_max = x[j]
                index_left_max = j
        x[index_left_max] = x[i]
        x[i] = left_max

    return x

print selection_sort(x)
