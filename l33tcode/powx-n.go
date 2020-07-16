package main

func myPow(x float64, n int) float64 {
	cache := map[int]float64{0: 1, 1: x, -1: 1/x}

	var dfs func(val float64, pow int) float64
	dfs = func(val float64, pow int) float64 {
		if _, ok := cache[pow]; !ok {
			cache[pow] = dfs(val, pow/2) * dfs(val, pow/2) * dfs(val, pow%2)
		}

		return cache[pow]
	}

	return dfs(x, n)
}
