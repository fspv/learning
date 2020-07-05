package main

func shipWithinDays(weights []int, D int) int {
	totalCargo := func(weights []int) int {
		cargo := 0

		for _, weight := range weights {
			cargo += weight
		}

		return cargo
	}

	maxWeight := func(weights []int) int {
		result := 0

		for _, weight := range weights {
			if weight > result {
				result = weight
			}
		}

		return result
	}

	daysToShip := func(weights []int, capacity int) int {
		cargo := 0
		days := 1

		for _, weight := range weights {
			if weight + cargo > capacity {
				days += 1
				cargo = weight
			} else {
				cargo += weight
			}
		}

		return days
	}

	bisect := func(weights []int, left int, right int, D int) int {
		for left < right {
			middle := (left + right) / 2
			days := daysToShip(weights, middle)

			if days > D {
				left = middle + 1
			} else {
				right = middle
			}
		}

		return right
	}

	return bisect(weights, maxWeight(weights), totalCargo(weights), D)
}
