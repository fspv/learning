package main

func allPathsSourceTarget(graph [][]int) [][]int {
	var dfs func(node int) *[][]int
	dfs = func(node int) *[][]int {
		result := [][]int{}

		if node == len(graph)-1 {
			path := []int{}
			path = append(path, node)
			result = append(result, path)

			return &result
		}

		for _, next_node := range graph[node] {
			paths := *dfs(next_node)
			for _, path := range paths {
				path = append(path, node)
				result = append(result, path)
			}
		}

		return &result
	}

	result := *dfs(0)

	for pos, _ := range result {
		for left, right := 0, len(result[pos])-1; left < right; {
			result[pos][left], result[pos][right] = result[pos][right], result[pos][left]
			left++
			right--
		}
	}

	return result
}
