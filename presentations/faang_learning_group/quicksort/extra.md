Partition schemes
=================

Lomuto partition scheme
-----------------------

Similar to the one we used


Hoare partition scheme
----------------------

Didn't have a chance to understand it, but it is on wikipedia.
Uses two pointers moving towards each other with some smart idea applied.
On overage does 3 times less swaps.

Optimisations
=============
* Recurse first to a smaller part of the partition and then use tail recursion for the other one
    - At most O(log n) space is used as a result
* When number of elements is below some threshold - fallback to non-recursive algorithm


Parallelization
===============

Divide-and-conquer => easy to parallel

Other quicksorts
================
* Paranoid quicksort (tries to partition until the certain level of imbalance is reached)
  Pivot ranges allowed:
  ```
    [ 1/4 | 1/4 | 1/4 | 1/4 ]
     |___| |_________| |___|
      bad     good      bad
  ```
  So cell is good with probability 1/2 => O(n log n) on average (proof is out of scope)
* Multi-pivot quicksort
* External quicksort
* Three-way radix quicksort
* Quick radix sort
* BlockQuicksort
* Partial and incremental quicksort (k-select)
