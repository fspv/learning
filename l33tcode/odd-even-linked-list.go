package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	var odd_end *ListNode
	var even_begin, even_end *ListNode
	node := head
	for count := 1; node != nil; count++ {
		node_next := node.Next
		if count%2 == 1 {
			if odd_end != nil {
				odd_end.Next = node
			}
			odd_end = node
			if even_begin != nil {
				odd_end.Next = even_begin
			}
		} else {
			if even_end == nil {
				even_begin = node
			} else {
				even_end.Next = node
			}
			even_end = node
			node.Next = nil
		}
		node = node_next
	}

	return head
}
