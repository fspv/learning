package main

import (
	"container/heap"
	"strings"
)

type CharCount struct {
	char  rune
	count int
}

type CharCountHeap []CharCount

func (heap CharCountHeap) Len() int {
	return len(heap)
}

func (heap CharCountHeap) Less(i, j int) bool {
	return heap[i].count > heap[j].count
}

func (heap CharCountHeap) Swap(i, j int) {
	heap[i], heap[j] = heap[j], heap[i]
}

func (heap *CharCountHeap) Push(item interface{}) {
	*heap = append(*heap, item.(CharCount))
}

func (heap *CharCountHeap) Pop() interface{} {
	old := *heap
	old_len := len(old)
	result := old[old_len-1]
	*heap = old[0 : old_len-1]

	return result
}

func calculateCharCounts(s string) map[rune]int {
	result := map[rune]int{}

	for _, char := range s {
		if val, ok := result[char]; ok {
			result[char] = val + 1
		} else {
			result[char] = 1
		}
	}

	return result
}

func reorganizeString(s string) string {
	var sb strings.Builder

	heapContainter := &CharCountHeap{}
	heap.Init(heapContainter)

	charCounts := calculateCharCounts(s)

	for char, count := range charCounts {
		heap.Push(heapContainter, CharCount{char, count})
	}

	prevCharCount := CharCount{'_', 0}

	for len(*heapContainter) > 0 {
		charCount := heap.Pop(heapContainter).(CharCount)
		sb.WriteRune(charCount.char)

		if prevCharCount.count > 0 {
			heap.Push(heapContainter, prevCharCount)
		}

		prevCharCount = CharCount{charCount.char, charCount.count - 1}
	}

	if prevCharCount.count > 0 {
		return ""
	}

	return sb.String()
}
