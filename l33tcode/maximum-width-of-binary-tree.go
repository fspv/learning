package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func widthOfBinaryTree(root *TreeNode) int {
	if root == nil {
		return 0
	}

	minOnLevel := map[int]int{}

	result := 1

	updateMin := func(level int, pos int) {
		_, ok := minOnLevel[level]

		if !ok {
			minOnLevel[level] = pos
		}

		if pos < minOnLevel[level] {
			minOnLevel[level] = pos
		}

		diff := pos - minOnLevel[level] + 1
		if diff > result {
			result = diff
		}
	}

	var dfs func(node *TreeNode, level int, pos int)
	dfs = func(node *TreeNode, level int, pos int) {
		if node.Left != nil {
			newPos := pos*2 + 1
			updateMin(level, newPos)
			dfs(node.Left, level+1, newPos)
		}
		if node.Right != nil {
			newPos := pos*2 + 2
			updateMin(level, newPos)
			dfs(node.Right, level+1, newPos)
		}
	}

	dfs(root, 0, 0)

	return result
}

func main() {
	root := &TreeNode{1, nil, nil}
	node := &TreeNode{2, nil, nil}
	root.Left = node
	widthOfBinaryTree(root)
}
