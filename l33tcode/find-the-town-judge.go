package main

func findJudge(N int, trust [][]int) int {
	if N == 1 && len(trust) == 0 {
		return 1
	}

	exempted := map[int]bool{}
	possible_judges := map[int]int{}

	for _, connection := range trust {
		from, to := connection[0], connection[1]
		exempted[from] = true
		delete(possible_judges, from)
		_, ok := exempted[to]

		if !ok {
			possible_judges[to] += 1
		}
	}

	if len(possible_judges) == 1 {
		for judge, count := range possible_judges {
			if count == N - 1 {
				return judge
			}
		}
	}

	return -1
}
