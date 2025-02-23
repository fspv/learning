package main

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func constructFromPrePost(preorder []int, postorder []int) *TreeNode {
    var dfs func() *TreeNode
	posPreorder, posPostorder := 0, 0

    dfs  = func() *TreeNode {
		if posPreorder == len(preorder) || posPostorder == len(postorder) {
			return nil
		}

		node := &TreeNode{Val: preorder[posPreorder]}
		posPreorder += 1

		if node.Val != postorder[posPostorder] {
			node.Left = dfs()
		}

		if node.Val != postorder[posPostorder] {
			node.Right = dfs()
		}

		posPostorder += 1

		return node
	}

	return dfs()
}
