General
=======

* Developed by British computer scientist **Tony Hoare** (while he was a visiting student at MSU) in 1959
* Published in 1961
* When implemented well, it
    - can be somewhat faster than merge sort
    - about two or three times faster than heapsort
* Randomized algorithm (usually implicitly randomized)

Idea
====

Uses divide-and-conquer algorithm.

On each step:

1. Randomly select a **pivot** element
2. Partition the other elements in 2 subarrays
    - less than pivot
    - greater than pivot
3. Recursively sort those subarrays


Time Complexity
==========

**On average:** O(n log n) comparisons

**Worst case:** O(n^2) comparisons

Space Complexity
================

O(1) additional memory (in-place)
