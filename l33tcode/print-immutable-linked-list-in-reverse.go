package main

type ImmutableListNode struct {
}

func (this *ImmutableListNode) getNext() ImmutableListNode {
   return *this
}

func (this *ImmutableListNode) printValue() {
   return
}

func printLinkedListInReverse(head ImmutableListNode) {
	stack := []ImmutableListNode{}

	for node := head; node != nil; node = node.getNext() {
		stack = append(stack, node)
	}

	for len(stack) > 0 {
		stack[len(stack) - 1].printValue()
		stack = stack[:len(stack) - 1]
	}

	return
}
