package main

import (
	"fmt"
	"strconv"
	"strings"
)

func findContestMatch(n int) string {
	array := make([]string, n)

	for pos, _ := range make([]int, n) {
		array[pos] = strconv.Itoa(pos + 1)
	}

	for power := 1; power < n; power *= 2 {
		tmp_arr := make([]string, n+n/power/2)
		for slice, _ := range make([]int, n/power/2) {
			start := slice * power
			copy(tmp_arr[start*2:start*2+power], array[start:start+power])
			copy(tmp_arr[start*2+power:start*2+power*2], array[n-start-power:n-start])
		}
		array = tmp_arr
	}

	var dfs func(array []string, output []string, pow int) []string
	pos := 0
	dfs = func(array []string, output []string, pow int) []string {
		if pow == 1 {
			output = append(output, array[pos])
			pos += 1
		} else {
			output = append(output, "(")
			output = dfs(array, output, pow/2)
			output = append(output, ",")
			output = dfs(array, output, pow/2)
			output = append(output, ")")
		}

		return output
	}

	output := []string{}

	output = dfs(array, output, n)

	return strings.Join(output, "")
}
