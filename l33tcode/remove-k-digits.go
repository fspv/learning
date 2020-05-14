package main

import (
	"strings"
)

func removeKdigits(num string, k int) string {
	stack := []rune{}
	removed := 0
	for _, digit := range num {
		for removed < k && len(stack) > 0 && digit < stack[len(stack) - 1] {
			stack = stack[:len(stack) - 1]
			removed += 1
		}
		stack = append(stack, digit)
	}
	result := strings.TrimLeft(string(stack[:len(num)-k]), "0")
	if result == "" {
		return "0"
	}
	return result
}
