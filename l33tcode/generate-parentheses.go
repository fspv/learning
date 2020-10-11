package main

func generateParenthesis(n int) []string {
	var dfs func(openParens int, closeParens int, arr []rune) []string
	dfs = func(openParens int, closeParens int, arr []rune) []string {
		result := []string{}
		if openParens == 0 && closeParens == 0 {
			result = append(result, string(arr))
		}

		if openParens > 0 {
			arr = append(arr, '(')
			for _, prev_result := range dfs(openParens-1, closeParens, arr) {
				result = append(result, prev_result)
			}
			arr = arr[:len(arr)-1]
		}

		if closeParens > 0 && closeParens > openParens {
			arr = append(arr, ')')
			for _, prev_result := range dfs(openParens, closeParens-1, arr) {
				result = append(result, prev_result)
			}
			arr = arr[:len(arr)-1]
		}

		return result
	}

	return dfs(n, n, []rune{})
}
