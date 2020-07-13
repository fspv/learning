package main

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	var dfs func(nodeLeft *TreeNode, nodeRight *TreeNode) bool
	dfs = func(nodeLeft *TreeNode, nodeRight *TreeNode) bool {
		if nodeLeft == nil && nodeRight == nil {
			return true
		}

		if nodeLeft == nil || nodeRight == nil {
			return false
		}

		if nodeLeft.Val != nodeRight.Val {
			return false
		}

		return dfs(nodeLeft.Left, nodeRight.Left) && dfs(nodeLeft.Right, nodeRight.Right)
	}

	return dfs(p, q)
}
