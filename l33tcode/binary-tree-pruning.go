package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pruneTree(root *TreeNode) *TreeNode {
	var dfs func(node *TreeNode) bool
	dfs = func(node *TreeNode) bool {
		if node == nil {
			return false
		}
		left, right := dfs(node.Left), dfs(node.Right)
		if !left {
			node.Left = nil
		}
		if !right {
			node.Right = nil
		}

		return left || right || node.Val == 1
	}

	if dfs(root) {
		return root
	}

	return nil
}
