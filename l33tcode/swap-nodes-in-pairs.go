package main

func removeNext(node *ListNode) {
	if node == nil {
		return
	}

	next := node.Next

	if next != nil {
		node.Next = next.Next
		next.Next = nil
	}
}

func insertAfter(node *ListNode, newNode *ListNode) {
	if node == nil {
		return
	}

	next := node.Next
	node.Next = newNode
	newNode.Next = next
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	dummy := &ListNode{}
	dummy.Next = head

	prev, first, second := dummy, head, head.Next

	for first != nil && second != nil {
		removeNext(first)
		insertAfter(prev, second)

		prev, first, second = first, first.Next, nil
		if first != nil {
			second = first.Next
		}
	}

	return dummy.Next
}
