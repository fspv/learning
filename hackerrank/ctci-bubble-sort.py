def countSwaps(a):
    swaps = 0

    for end_pos in reversed(range(len(a))):
        for pos in range(end_pos):
            if a[pos] > a[pos + 1]:
                a[pos], a[pos + 1] = a[pos + 1], a[pos]
                swaps += 1

    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
