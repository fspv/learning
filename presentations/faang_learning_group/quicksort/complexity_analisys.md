Basic quicksort
===============

In the worst case, each step we select a pivot, so
1. One side has `n - 1` elements
2. Other has `0` elements

So basically the array is sorted or reverse sorted.

If we apply the master theorem

```
T(n) = T(0) + T(n - 1) + Theta(n)
T(n) = Theta(1) + T(n - 1) + Theta(n)
T(n) = T(n - 1) + Theta(n)
T(n) = Theta(n^2)  => O(n^2)
```

Can we do better?
=================

* Median selection algorithm, with O(n) time complexity

In this case, we always divide the array in 2 equal parts, so master theorem becomes:

```
T(n) = 2 * T(n / 2) + Theta(n) + Theta(n)
T(n) = Theta(n log n)  =>  O(n log n)
```

Cons: median selection algorithm is hard to implement

Randomized Quicksort (Las Vegas)
================================

* Pivot is chosen at random from the array

Expected time: O(n log n)
