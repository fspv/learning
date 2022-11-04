package main

import "sort"

type Flower struct {
	PlantTime int
	GrowTime  int
}

type ByGrowTime []Flower

func (a ByGrowTime) Len() int           { return len(a) }
func (a ByGrowTime) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByGrowTime) Less(i, j int) bool { return a[i].GrowTime < a[j].GrowTime }

func earliestFullBloom(plantTime []int, growTime []int) int {
	flowers := []Flower{}

	for i, _ := range plantTime {
		flowers = append(flowers, Flower{plantTime[i], growTime[i]})
	}

	sort.Sort(ByGrowTime(flowers))

	var result int

	result = 0

	for _, flower := range flowers {
		if flower.PlantTime < result {
			result += flower.GrowTime
		} else {
			result = flower.PlantTime + flower.GrowTime
		}
	}

	return result
}
