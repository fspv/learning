package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	var dfs func(node *TreeNode) *TreeNode
	dfs = func(node *TreeNode) *TreeNode {
		if node != nil {
			node.Left, node.Right = dfs(node.Right), dfs(node.Left)
		}

		return node
	}

	return dfs(root)
}
