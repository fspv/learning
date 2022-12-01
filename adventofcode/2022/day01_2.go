package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"log"
	"os"
	"strconv"
)

type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
	last := (*h)[len(*h)-1]

	*h = (*h)[:len(*h)-1]

	return last
}

func day1_2() {
	file, err := os.Open("day01_1.input")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	soFar := 0
	h := &IntHeap{}
	heap.Init(h)

	for scanner.Scan() {
		text := scanner.Text()

		if text == "" {
			heap.Push(h, soFar)

			if h.Len() > 3 {
				heap.Pop(h)
			}

			soFar = 0
		} else {
			value, err := strconv.Atoi(text)

			if err != nil {
				log.Fatal(err)
			}

			soFar += value
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	total := 0

	for _, num := range *h {
		total += num
	}

	fmt.Println(total)
}
