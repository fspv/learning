package main

func dailyTemperatures(temperatures []int) []int {
	stack := []int{}
	answer := []int{}

	for pos, _ := range temperatures {
		posBack := len(temperatures) - pos - 1

		for len(stack) > 0 && temperatures[stack[len(stack)-1]] <= temperatures[posBack] {
			stack = stack[:len(stack)-1]
		}

		if len(stack) > 0 {
			answer = append(answer, stack[len(stack)-1]-posBack)
		} else {
			answer = append(answer, 0)
		}

		stack = append(stack, posBack)
	}

	for pos, _ := range make([]int, len(answer)/2) {
		posBack := len(answer) - pos - 1

		answer[pos], answer[posBack] = answer[posBack], answer[pos]
	}

	return answer
}
