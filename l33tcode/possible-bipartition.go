package main

func color(node int, adjList [][]int, colors []int, visited []bool) bool {
	visited[node] = true

	for _, adjNode := range adjList[node] {
		if colors[node] == 0 && colors[adjNode] == 0 {
			colors[node] = 1
			colors[adjNode] = 2
		}

		if colors[node] == 1 {
			if colors[adjNode] == 2 || colors[adjNode] == 0 {
				colors[adjNode] = 2

				if visited[adjNode] {
					continue
				}

				if !color(adjNode, adjList, colors, visited) {
					return false
				}
			} else {
				return false
			}
		}

		if colors[node] == 2 {
			if colors[adjNode] == 1 || colors[adjNode] == 0 {
				colors[adjNode] = 1

				if visited[adjNode] {
					continue
				}

				if !color(adjNode, adjList, colors, visited) {
					return false
				}
			} else {
				return false
			}
		}
	}
	return true
}

func possibleBipartition(n int, dislikes [][]int) bool {
	colors := make([]int, n)
	visited := make([]bool, n)

	adjList := make([][]int, n)

	for _, dislike := range dislikes {
		src, dst := dislike[0]-1, dislike[1]-1

		adjList[src] = append(adjList[src], dst)
		adjList[dst] = append(adjList[dst], src)
	}

	for node, _ := range make([]int, n) {
		if !color(node, adjList, colors, visited) {
			return false
		}
	}

	return true
}
