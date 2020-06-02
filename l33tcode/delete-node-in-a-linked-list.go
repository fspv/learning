package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteNode(node *ListNode) {
	for curNode := node; curNode.Next != nil; curNode = curNode.Next {
		curNode.Val = curNode.Next.Val
		if curNode.Next.Next == nil {
			curNode.Next = nil
			break
		}
	}
}
