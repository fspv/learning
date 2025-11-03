package main

import "slices"

type Allocator struct {
	allocated   map[int]int
	free        map[int]int
	allocations map[int][]int
}

func Constructor(n int) Allocator {
	return Allocator{
		allocated: map[int]int{},
		free: map[int]int{
			0: n,
		},
		allocations: map[int][]int{},
	}
}

func (this *Allocator) Allocate(size int, mID int) int {
	// get a list of sorted free blocks

	freeBlocks := []int{}

	for offset := range this.free {
		freeBlocks = append(freeBlocks, offset)
	}

	slices.Sort(freeBlocks)

	// find first suitable allocation
	// If found
	//   0. Add allocation to allocations
	//   1. Remove block from free
	//   2. Add block of the requested size to allocated
	//   3. If there is still some space left, add it back to free

	for _, free_offset := range freeBlocks {
		if this.free[free_offset] < size {
			continue
		}

		free_size := this.free[free_offset]

		if _, ok := this.allocations[mID]; !ok {
			this.allocations[mID] = []int{}
		}

		this.allocations[mID] = append(this.allocations[mID], free_offset)
		delete(this.free, free_offset)
		this.allocated[free_offset] = size

		if free_size == size {
			return free_offset
		}

		this.free[free_offset+size] = free_size - size
		return free_offset
	}

	// if not found
	return -1
}

func (this *Allocator) FreeMemory(mID int) int {
	// remove all the allocation with mid
	// for each removed allocation:
	//   1. Remove it from allocated blocks
	//   2. Add it back to the free map
	//   3. If there are adjacent free elements, merge them together

	freed := 0

	allocations, ok := this.allocations[mID]
	if !ok {
		return 0
	}
	delete(this.allocations, mID)

	for _, offset := range allocations {
		size := this.allocated[offset]
		delete(this.allocated, offset)

		this.free[offset] = size
		freed += size

		if next_size, ok := this.free[offset+size]; ok {
			this.free[offset] += next_size
			delete(this.free, offset+size)
		}

		offsetToRemove := -1
		for prev_offset, prev_size := range this.free {
			if prev_offset+prev_size == offset {
				offsetToRemove = prev_offset
			}
		}

		if offsetToRemove != -1 {
			this.free[offsetToRemove] += this.free[offset]
			delete(this.free, offset)
		}
	}

	return freed
}
