/*
Идея: Используем алгоритм Таржана для того, чтобы найти все сильно связанные компоненты
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
Когда все articulation points найдены, мы можем раскрасить граф (каждую компоненту в свой цвет).
После этого, используя цвета, можно построить дерево, узлами которого будут являться бывшие связанные компоненты.
После этого не составит труда найти самый длинный путь в дереве, если отсортировать все вершины по убыванию и пытаться из их по одному ребру нарастить такой путь вниз (простейший вариант динамического программирования).

Итоговая сложность получится:

* Построение компонент: O(V + E) по времени и памяти
* Раскрашивание: O(V + E) по времени и памяти
* Сортировка для вывода весов и нахождения длиннейшего пути: O(V log) по времени
* Нахождение длиннейшего пути и вывод: O(V + E) по времени и памяти

Итого полная сложность выходит O(V log V + E) по времени, O(V + E) по памяти
*/
package main

import "fmt"
import "sort"
import "bufio"
import "os"

// Just helper methods and definitions
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }

type IntArray []int

func (array IntArray) Len() int {
	return len(array)
}

func (array IntArray) Less(i, j int) bool {
	return array[i] < array[j]
}

func (array IntArray) Swap(i, j int) {
	array[i], array[j] = array[j], array[i]
}

// Colors used during the DFS
// WHITE - not visited
// GRAY - in the recursion stack
// BLACK - all the children are visited, removed from the stack
type Color int64

const (
	WHITE Color = iota
	GRAY
	BLACK
)

type Vertex struct {
	label                    int    // Position from the input
	weight                   int    // A number from the input
	enterTimestamp           int    // Timestamp when we first seen the vertex
	lowestReachableTimestamp int    // Lowest enter timestamp reachable from here (by back edges)
	dfsColor                 Color  // Color used during dfs
	adj                      Graph  // A list of adjacent vertices
	adjRemoved               []bool // Indicated an edge has been temporarily removed
	color                    int    // Color of a biconnected component (each component has its own assigned)
}

type Graph []*Vertex

func (vertices Graph) Len() int {
	return len(vertices)
}

func (vertices Graph) Less(i, j int) bool {
	return vertices[i].weight < vertices[j].weight
}

func (vertices Graph) Swap(i, j int) {
	vertices[i], vertices[j] = vertices[j], vertices[i]
}

func newVertex(label int, weight int) *Vertex {
	// Helps create a vertex
	return &Vertex{label, weight, 0, 0, WHITE, Graph{}, []bool{}, -1}
}

func find(array Graph, target *Vertex) int {
	/* Finds the position of the target in the array */
	toRemove := -1

	for pos, val := range array {
		if val.label == target.label {
			toRemove = pos
			break
		}
	}

	return toRemove
}

func dfs(vertex *Vertex, timestamp int) int {
	/*
		Dfs that sets timestamps used in Tarjan's algorithm
		to find articulation points
	*/
	vertex.dfsColor = GRAY
	vertex.enterTimestamp = timestamp
	vertex.lowestReachableTimestamp = timestamp

	timestamp++

	for nextPos, nextVertex := range vertex.adj {
		if vertex.adjRemoved[nextPos] {
			continue
		}
		if nextVertex.dfsColor == GRAY {
			// We have a back edge
			if vertex.lowestReachableTimestamp > nextVertex.enterTimestamp {
				vertex.lowestReachableTimestamp = nextVertex.enterTimestamp
			}
		} else if nextVertex.dfsColor == WHITE {
			// We have a new tree edge
			toRemove := find(nextVertex.adj, vertex)
			nextVertex.adjRemoved[toRemove] = true
			timestamp = dfs(nextVertex, timestamp)
			nextVertex.adjRemoved[toRemove] = false

			if vertex.lowestReachableTimestamp > nextVertex.lowestReachableTimestamp {
				vertex.lowestReachableTimestamp = nextVertex.lowestReachableTimestamp
			}

		}
	}

	vertex.dfsColor = BLACK

	return timestamp
}

func paint(vertex *Vertex, color int, maxColor int) int {
	/*
		Color the graph with respect to the articulation points.
		If we find a bridge which connects two biconnected
		components, we don't follow such a bridge, so we will
		color only current component
	*/
	vertex.dfsColor = GRAY
	vertex.color = color

	for _, adjVertex := range vertex.adj {
		// Already processed

		if adjVertex.dfsColor != WHITE {
			continue
		}

		if adjVertex.lowestReachableTimestamp > vertex.enterTimestamp {
			// This is an articulation point, should switch to
			// the next color
			tmp := paint(adjVertex, maxColor+1, maxColor+1)
			if tmp > maxColor {
				maxColor = tmp
			}
		} else {
			// Not an articulation point, need to use the same color
			tmp := paint(adjVertex, color, maxColor)
			if tmp > maxColor {
				maxColor = tmp
			}
		}
	}
	vertex.dfsColor = BLACK

	return maxColor
}

func biconnectComponents(vertices Graph) {
	/*
		Find all biconnected components
	*/
	timestamp := 0

	// Set dfs timestamps
	for _, vertex := range vertices {
		if vertex.dfsColor == WHITE {
			timestamp = dfs(vertex, timestamp)
		}
	}

	// Reset dfs timestamps
	for _, vertex := range vertices {
		vertex.dfsColor = WHITE
	}

	// Paint components
	color := 0
	for _, vertex := range vertices {
		if vertex.color == -1 {
			color = paint(vertex, color, color) + 1
		}
	}
}

func buildCompressedGraph(vertices Graph) Graph {
	/*
		Given a biconnected graph, build a condensed version of it
	*/
	colors := 0

	for _, vertex := range vertices {
		if vertex.color+1 > colors {
			colors = vertex.color + 1
		}
	}

	compressedVertices := make(Graph, colors)
	for pos := 0; pos < colors; pos++ {
		compressedVertices[pos] = newVertex(pos+1, 0)
		compressedVertices[pos].color = pos
	}

	for _, vertex := range vertices {
		compressedVertices[vertex.color].weight += vertex.weight

		for _, adjVertex := range vertex.adj {
			if vertex.color == adjVertex.color {
				continue
			}

			compressedVertices[vertex.color].adj = append(compressedVertices[vertex.color].adj, compressedVertices[adjVertex.color])
		}
	}

	return compressedVertices
}

func dfsDepth(vertex *Vertex, asc bool) int {
	/*
		Try to follow the graph in ascending (descending) weights order
		and calculate the maximum depth reachable
	*/
	vertex.dfsColor = GRAY

	maxDepth := 0

	for _, adjVertex := range vertex.adj {
		if asc && adjVertex.weight > vertex.weight {
			depth := dfsDepth(adjVertex, asc)

			if depth > maxDepth {
				maxDepth = depth
			}
		}
		if !asc && adjVertex.weight < vertex.weight {
			depth := dfsDepth(adjVertex, asc)

			if depth > maxDepth {
				maxDepth = depth
			}
		}
	}

	vertex.dfsColor = BLACK

	return maxDepth + 1
}

func longestPath(vertices Graph) int {
	/*
		Get the longest path which is strictly ascending (descending)
	*/
	paths := make([]int, len(vertices))

	for pos, _ := range vertices {
		paths[pos] = 1
	}

	for pos, _ := range vertices {
		vertex := vertices[len(vertices)-pos-1]
		for _, adjVertex := range vertex.adj {
			if vertex.weight > adjVertex.weight {
				if paths[vertex.label-1]+1 > paths[adjVertex.label-1] {
					paths[adjVertex.label-1] = paths[vertex.label-1] + 1
				}
			}
		}
	}

	maxPath := 1
	for _, path := range paths {
		if path > maxPath {
			maxPath = path
		}
	}
	return maxPath
}

func componentPath(vertices Graph) (Graph, int) {
	biconnectComponents(vertices)
	compressedVertices := buildCompressedGraph(vertices)
	sort.Sort(compressedVertices)

	return compressedVertices, longestPath(compressedVertices)
}

func main() {
	defer writer.Flush()

	var numVertices, numEdges int

	scanf("%d %d\n", &numVertices, &numEdges)

	vertices := make(Graph, numVertices)

	for pos := 0; pos < numVertices; pos++ {
		var weight int
		scanf("%d", &weight)
		vertices[pos] = newVertex(pos+1, weight)
	}

	scanf("\n")

	for pos := 0; pos < numEdges; pos++ {
		var src, dst int
		scanf("%d %d\n", &src, &dst)

		vertices[src-1].adj = append(vertices[src-1].adj, vertices[dst-1])
		vertices[src-1].adjRemoved = append(vertices[src-1].adjRemoved, false)
		vertices[dst-1].adj = append(vertices[dst-1].adj, vertices[src-1])
		vertices[dst-1].adjRemoved = append(vertices[dst-1].adjRemoved, false)
	}

	compressedVertices, longestCompressedPath := componentPath(vertices)

	for _, vertex := range compressedVertices {
		printf("%d ", vertex.weight)
	}
	printf("\n")

	printf("%d\n", longestCompressedPath)
}
