package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func insertionSortList(head *ListNode) *ListNode {
	fakeHead := &ListNode{} // just a node with no value, we'll never check it
	fakeHead.Next = head

	prevNode := fakeHead
	node := fakeHead.Next

	for node != nil {
		prevNodeInsert := fakeHead
		nodeInsert := fakeHead.Next

		for nodeInsert != nil && nodeInsert.Val < node.Val && nodeInsert != node {
			prevNodeInsert = nodeInsert
			nodeInsert = nodeInsert.Next
		}

		nodeNext := node.Next

		if nodeInsert != node {
			prevNodeInsert.Next = node

			node.Next = nodeInsert

			prevNode.Next = nodeNext
		} else {
			prevNode = node
		}

		node = nodeNext
	}

	return fakeHead.Next
}
