/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *	 Val int
 *	 Left *TreeNode
 *	 Right *TreeNode
 * }
 */
package main

func isCousins(root *TreeNode, x int, y int) bool {
	var dfs func(node *TreeNode, x int, y int) (int, bool)
	dfs = func(node *TreeNode, x int, y int) (int, bool) {
		if node == nil {
			return 0, false
		}
		if node.Val == x || node.Val == y {
			return 1, false
		}
		left_count, left_cousins := dfs(node.Left, x, y)
		right_count, right_cousins := dfs(node.Right, x, y)

		if left_count != 0 && right_count != 0 {
			if left_count == right_count && left_count > 1 {
				return 0, true
			} else {
				return 0, false
			}
		} else if left_count != 0 {
			return left_count + 1, false
		} else if right_count != 0 {
			return right_count + 1, false
		}
		return 0, left_cousins || right_cousins
	}

	_, result := dfs(root, x, y)

	return result
}
