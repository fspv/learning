package main

import "sync"

type FenwickTree struct {
	bitSums []int
	mu sync.RWMutex
}

func NewFenwickTree(size int) *FenwickTree {
	return &FenwickTree{
		bitSums: make([]int, size + 1),
	}
}

func leastSignificantBit(num int) int {
	return num & (-num)
}

func (t *FenwickTree) Sum(pos int) int {
	t.mu.RLock()
	defer t.mu.RUnlock()

	pos += 1

	sum := 0

	for pos > 0 {
		sum += t.bitSums[pos]
		pos -= leastSignificantBit(pos)
	}

	return sum
}

func (t *FenwickTree) Add(pos int, value int) {
	t.mu.Lock()
	defer t.mu.Unlock()

	pos += 1

	for pos < len(t.bitSums) {
		t.bitSums[pos] += value
		pos += leastSignificantBit(pos)
	}
}

type MRUQueue struct {
	fenwickTree *FenwickTree
	elements []int
}


func Constructor(n int) MRUQueue {
	q := MRUQueue{
    	fenwickTree: NewFenwickTree(n + 2000 + 1),
		elements: make([]int, n),
    }

	for i := range make([]bool, n) {
		q.elements[i] = i + 1
		q.fenwickTree.Add(i, 1)
	}

	return q
}

func (this *MRUQueue) Fetch(k int) int {
	// Search where the kth element is in the sparse array
	left, right := 0, len(this.elements)

	for left < right {
		mid := left + (right - left) / 2

		if this.fenwickTree.Sum(mid) < k {
			left = mid + 1
		} else {
			right = mid
		}
	}

	pos := left

	// Remove element from the current pos (no need to actually remove it,
	// we'll never access it again)
	this.fenwickTree.Add(pos, -1)

	// Extend the array and move element to the end
	this.elements = append(this.elements, this.elements[pos])
	this.fenwickTree.Add(len(this.elements) - 1, 1)

	return this.elements[pos]
}
