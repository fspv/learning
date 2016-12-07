from random import randint

x = [ randint(0, 100) for i in xrange(0, 100) ]


def merge(left, right):
    out = []

    l_left = len(left)
    l_right = len(right)

    left += [ 9999999999 ]
    right += [ 9999999999 ]

    left_c = 0
    right_c = 0

    for i in xrange(l_left + l_right):
        if left[left_c] <= right[right_c]:
            out += [ left[left_c] ]
            left_c += 1
        else:
            out += [ right[right_c] ]
            right_c += 1

    return out


def merge_sort(x, p, r):
    q = (p + r) / 2
    if r > p:
        left = merge_sort(x, p, q)
        right = merge_sort(x, q + 1, r)
        return merge(left, right)
    else:
        return [ x[p] ]


p = 0
r = len(x) - 1

print(x)
print(sorted(x))
print(merge_sort(x, p, r))
