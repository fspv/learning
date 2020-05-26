package main

type StackItem struct {
	price  int
	weight int
}

type StockSpanner struct {
	stack []StackItem
}

func Constructor() StockSpanner {
	return StockSpanner{stack: []StackItem{}}
}

func (this *StockSpanner) Next(price int) int {
	weight := 1
	for len(this.stack) > 0 && this.stack[len(this.stack)-1].price <= price {
		weight += this.stack[len(this.stack)-1].weight
		this.stack = this.stack[:len(this.stack)-1]
	}
	this.stack = append(this.stack, StackItem{price: price, weight: weight})

	return weight
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
