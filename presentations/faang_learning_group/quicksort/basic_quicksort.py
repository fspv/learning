from typing import List


def quicksort(array: List[int], left: int, right: int) -> None:
    if left >= right:
        return

    #####################
    # 1. Select a pivot #
    #####################

    pivot = array[right - 1]  # select the rightmost (non-randomized algorithm)

    ################
    # 2. Partition #
    ################

    # Partition starts at the left element, before we
    # start scanning the array
    partition = left

    for pos in range(left, right):
        if array[pos] <= pivot:
            # Add the element below the pivot to partition and increase
            # the partition size
            array[pos], array[partition] = array[partition], array[pos]  # swap
            partition += 1

    # At this point pivot element is located in the correct place

    ######################
    # 3. Sort partitions #
    ######################

    # Recurse to the partitioned data to sort it as well
    quicksort(array, left, partition - 1)
    quicksort(array, partition, right)
