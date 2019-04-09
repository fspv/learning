def rotLeft(a, d):
    shift = d % len(a)

    return a[shift:] + a[:shift]
