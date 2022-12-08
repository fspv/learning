package main

type UnionFind struct {
	counts []int
	roots  []int
}

func (set *UnionFind) init() {
	for pos, _ := range set.roots {
		set.roots[pos] = pos
		set.counts[pos] = 1
	}
}

func (set *UnionFind) union(rootLeft, rootRight int) {
	rootLess, rootMore := rootLeft, rootRight

	if set.counts[rootLeft] > set.counts[rootRight] {
		rootLess, rootMore = rootMore, rootLess
	}

	set.roots[rootLess] = set.roots[rootMore]
	set.counts[rootMore] += set.counts[rootLess]
}

func (set *UnionFind) find(node int) int {
	if set.roots[node] == node {
		return node
	}

	set.roots[node] = set.find(set.roots[node])

	return set.roots[node]
}

func countComponents(n int, edges [][]int) int {
	set := UnionFind{make([]int, n), make([]int, n)}
	set.init()

	components := n

	for _, edge := range edges {
		src, dst := edge[0], edge[1]

		rootSrc, rootDst := set.find(src), set.find(dst)

		if rootSrc != rootDst {
			set.union(rootSrc, rootDst)
			components -= 1
		}

	}

	return components
}
