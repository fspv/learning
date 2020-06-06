package main

import (
	"sort"
)

type People [][]int

func (person People) Len() int {
	return len(person)
}
func (person People) Swap(i, j int) {
	person[i], person[j] = person[j], person[i]
}
func (person People) Less(i, j int) bool {
	return person[i][0] < person[j][0] || (person[i][0] == person[j][0] && person[i][1] < person[j][1])
}

func reconstructQueue(people [][]int) [][]int {
	sort.Sort(People(people))

	result := [][]int{}
	null_person := []int{-1, -1}
	for i := 0; i < len(people); i++ {
		result = append(result, null_person)
	}

	for _, person := range people {
		height, before := person[0], person[1]
		pos := 0
		for before > 0 || result[pos][0] != -1 {
			if result[pos][0] >= height || result[pos][0] == -1{
				before -= 1
			}
			pos += 1
		}
		result[pos] = person
	}

	return result
}
