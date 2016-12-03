from random import randint

x = sorted([ randint(0, 100) for i in xrange(0, 100) ])
search = 32

found = -1
p = 0
r = len(x) - 1

while found == -1 and r > p:
    q = p + (r - p) / 2
    if x[q] == search:
        found = q
    if x[q] < search:
        p = q + 1
    elif x[q] > search:
        r = q - 1

print x
print found
