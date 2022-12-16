package main

type MyQueue struct {
	stackLeft  []int
	stackRight []int
}

func Constructor() MyQueue {
	return MyQueue{[]int{}, []int{}}
}

func (this *MyQueue) Push(x int) {
	this.stackLeft = append(this.stackLeft, x)
}

func (this *MyQueue) Pop() int {
	for len(this.stackLeft) != 0 {
		this.stackRight = append(this.stackRight, this.stackLeft[len(this.stackLeft)-1])
		this.stackLeft = this.stackLeft[0 : len(this.stackLeft)-1]
	}

	result := this.stackRight[len(this.stackRight)-1]

	this.stackRight = this.stackRight[0 : len(this.stackRight)-1]

	for len(this.stackRight) != 0 {
		this.stackLeft = append(this.stackLeft, this.stackRight[len(this.stackRight)-1])
		this.stackRight = this.stackRight[0 : len(this.stackRight)-1]
	}

	return result
}

func (this *MyQueue) Peek() int {
	return this.stackLeft[0]
}

func (this *MyQueue) Empty() bool {
	return len(this.stackLeft) == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
