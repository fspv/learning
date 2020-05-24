package main

func numTeams(rating []int) int {
	teams := 0
	for middle := 1; middle < len(rating)-1; middle++ {
		left_less, left_more := 0, 0
		right_less, right_more := 0, 0
		for pos, _ := range make([]int, len(rating)) {
			if rating[pos] < rating[middle] {
				if pos < middle {
					left_less++
				} else {
					right_less++
				}
			} else if rating[pos] > rating[middle] {
				if pos < middle {
					left_more++
				} else {
					right_more++
				}
			}
		}
		teams += left_less*right_more + left_more*right_less
	}
	return teams
}
