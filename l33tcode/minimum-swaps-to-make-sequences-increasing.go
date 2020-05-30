package main

func minSwap(A []int, B []int) int {
	swapsRev, swapsSame := 1, 0

	for pos := 1; pos < len(A); pos++ {
		if A[pos-1] >= B[pos] || B[pos-1] >= A[pos] {
			swapsRev++
		} else if A[pos-1] >= A[pos] || B[pos-1] >= B[pos] {
			swapsRev, swapsSame = swapsSame+1, swapsRev
		} else {
			if swapsRev < swapsSame {
				swapsRev, swapsSame = swapsRev+1, swapsRev
			} else {
				swapsRev, swapsSame = swapsSame+1, swapsSame
			}
		}
	}

	result := 0

	if swapsRev < swapsSame {
		result = swapsRev
	} else {
		result = swapsSame
	}

	return result
}
