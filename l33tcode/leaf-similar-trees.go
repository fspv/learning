package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(node *TreeNode, arr *[]int) *[]int {
	if node.Left != nil {
		arr = dfs(node.Left, arr)
	}
	if node.Left == nil && node.Right == nil {
		*arr = append(*arr, node.Val)
	}
	if node.Right != nil {
		arr = dfs(node.Right, arr)
	}
	return arr
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	arr1 := &[]int{}
	arr2 := &[]int{}

	if root1 != nil {
		arr1 = dfs(root1, arr1)
	}
	if root2 != nil {
		arr2 = dfs(root2, arr2)
	}

	if len(*arr1) != len(*arr2) {
		return false
	}

	for pos, _ := range *arr1 {
		if (*arr1)[pos] != (*arr2)[pos] {
			return false
		}
	}

	return true
}
