package main

import "strconv"

func evalRPN(tokens []string) int {
	stack := []string{}

	for _, token := range tokens {
		left, right := "", ""

		if len(stack) >= 2 {
			left, right = stack[len(stack)-2], stack[len(stack)-1]
		}

		switch token {
		case "+":
			leftInt, _ := strconv.Atoi(left)
			rightInt, _ := strconv.Atoi(right)
			stack = stack[:len(stack)-2]

			stack = append(stack, strconv.Itoa(leftInt+rightInt))
		case "-":
			leftInt, _ := strconv.Atoi(left)
			rightInt, _ := strconv.Atoi(right)
			stack = stack[:len(stack)-2]

			stack = append(stack, strconv.Itoa(leftInt-rightInt))
		case "/":
			leftInt, _ := strconv.Atoi(left)
			rightInt, _ := strconv.Atoi(right)
			stack = stack[:len(stack)-2]

			stack = append(stack, strconv.Itoa(leftInt/rightInt))
		case "*":
			leftInt, _ := strconv.Atoi(left)
			rightInt, _ := strconv.Atoi(right)
			stack = stack[:len(stack)-2]

			stack = append(stack, strconv.Itoa(leftInt*rightInt))
		default:
			stack = append(stack, token)
		}
	}

	result, _ := strconv.Atoi(stack[0])

	return result
}
