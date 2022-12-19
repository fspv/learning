package main

func buildAdjList(nodes int, edges [][]int) [][]int {
	adjList := make([][]int, nodes)

	for _, edge := range edges {
		u, v := edge[0], edge[1]

		adjList[u] = append(adjList[u], v)
		adjList[v] = append(adjList[v], u)
	}

	return adjList
}

func dfs(source int, destination int, adjList *[][]int, visited *[]bool) bool {
	(*visited)[source] = true

	if source == destination {
		return true
	}

	for _, nextNode := range (*adjList)[source] {
		if (*visited)[nextNode] {
			continue
		}

		if dfs(nextNode, destination, adjList, visited) {
			return true
		}
	}

	return false
}

func validPath(n int, edges [][]int, source int, destination int) bool {
	adjList := buildAdjList(n, edges)
	visited := make([]bool, n)

	return dfs(source, destination, &adjList, &visited)
}
