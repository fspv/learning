package main

func pathSum(nums []int) int {
	parent := func(pos int) int {
		return (pos - 1) / 2
	}

	lvlOffset := func(lvl int) int {
		// expect lvl will be always non-negative
		return int((1 << uint(lvl)) - 1)
	}

	sums := make([]int, lvlOffset(4))
	isLeaf := make([]bool, lvlOffset(4))
	empty := make([]bool, lvlOffset(4))

	for pos := range isLeaf {
		isLeaf[pos] = true
		empty[pos] = true
	}

	for _, num := range nums {
		lvl, posWithinLvl, val := num/100-1, (num/10)%10-1, num%10
		pos := lvlOffset(lvl) + posWithinLvl
		curParent := parent(pos)
		sums[pos] = val + sums[curParent]
		empty[pos] = false
		if pos != 0 {
			isLeaf[curParent] = false
		}
	}

	result := 0

	for pos := range sums {
		if !empty[pos] && isLeaf[pos] {
			result += sums[pos]
		}
	}

	return result
}
