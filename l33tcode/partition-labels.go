package main

import (
	"math"
)

func partitionLabels(S string) []int {
	intervals := [][2]float64{}
	char_to_interval := map[rune]int{}

	for pos, char := range S {
		interval, ok := char_to_interval[char]
		if ok {
			intervals[interval][1] = float64(pos)
		} else {
			new_interval := [2]float64{}
			new_interval[0] = float64(pos)
			new_interval[1] = float64(pos)
			intervals = append(intervals, new_interval)
			char_to_interval[char] = len(intervals) - 1
		}
	}

	merged_intervals := [][2]float64{}
	merged_intervals = append(merged_intervals, intervals[0])
	for _, interval := range intervals {
		prev_end, cur_begin := merged_intervals[len(merged_intervals)-1][1], interval[0]
		if cur_begin <= prev_end {
			merged_intervals[len(merged_intervals)-1][1] = math.Max(
				merged_intervals[len(merged_intervals)-1][1], interval[1],
			)
		} else {
			merged_intervals = append(merged_intervals, interval)
		}
	}

	result := []int{}

	for _, interval := range merged_intervals {
		result = append(result, int(interval[1]-interval[0])+1)
	}

	return result
}
