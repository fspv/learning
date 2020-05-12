package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumEvenGrandparent(root *TreeNode) int {
	var dfs func(node *TreeNode, parent int, grandparent int) int
	dfs = func(node *TreeNode, parent int, grandparent int) int {
		if node == nil {
			return 0
		}
		result := 0
		if grandparent%2 == 0 {
			result = node.Val
		}
		result += dfs(node.Left, node.Val, parent)
		result += dfs(node.Right, node.Val, parent)

		return result
	}
	return dfs(root, 1, 1)
}
