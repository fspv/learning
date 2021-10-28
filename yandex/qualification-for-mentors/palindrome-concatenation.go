package main

import "fmt"
import "sort"

type Pairs [][]int

func (array Pairs) Len() int {
	return len(array)
}

func (array Pairs) Less(i, j int) bool {
	if array[i][0] < array[j][0] {
		return true
	} else if array[i][0] == array[j][0] {
		if array[i][1] < array[j][1] {
			return true
		}
	}

	return false
}

func (array Pairs) Swap(i, j int) {
	array[i], array[j] = array[j], array[i]
}

type TrieNode struct {
	children map[rune]*TrieNode
	end      bool
	word     int
}

func manacher(word string, leftOffset int) []bool {
	left, right := 0, -1
	cache := make([]int, len(word))

	result := make([]bool, len(word)+1)
	for pos, _ := range result {
		result[pos] = false
	}

	for pos, _ := range word {
		radius := 0

		if pos > right {
			radius = 1 - leftOffset
		} else {
			if cache[left+right-(pos-leftOffset)]+1 < right-pos+1 {
				radius = cache[left+right-(pos-leftOffset)] + 1
			} else {
				radius = right - pos + 1
			}
		}

		for 0 <= pos-leftOffset-radius && pos+radius < len(word) && word[pos-leftOffset-radius] == word[pos+radius] {
			radius++
		}

		radius -= 1

		cache[pos] = radius

		if pos+radius == len(word)-1 {
			result[pos-leftOffset-radius] = true
		}

		if pos+radius > right {
			left = pos - leftOffset - radius
			right = pos + radius
		}
	}

	return result
}

func isPalindromeFrom(word string) []bool {
	notShifted := manacher(word, 0)
	shiftedByOne := manacher(word, 1)

	result := make([]bool, len(word))

	for pos, _ := range word {
		result[pos] = notShifted[pos] || shiftedByOne[pos]
	}

	result = append(result, true)

	return result
}

func buildTrie(strings []string) *TrieNode {
	trieRoot := &TrieNode{map[rune]*TrieNode{}, false, -1}

	for wordPos, word := range strings {
		trieNode := trieRoot

		for _, char := range word {
			if _, ok := trieNode.children[char]; !ok {
				trieNode.children[char] = &TrieNode{map[rune]*TrieNode{}, false, -1}
			}

			trieNode = trieNode.children[char]
		}

		trieNode.end = true
		trieNode.word = wordPos

	}

	return trieRoot
}

func searchTrie(word string, isPalindrome []bool, trieRoot *TrieNode) []int {
	trieNode := trieRoot
	result := []int{}

	if trieNode.end && isPalindrome[0] {
		result = append(result, trieNode.word)
	}

	for pos, char := range word {
		if val, ok := trieNode.children[char]; ok {
			trieNode = val
		} else {
			break
		}

		if isPalindrome[pos+1] && trieNode.end {
			result = append(result, trieNode.word)
		}
	}

	return result
}

func reverseString(str string) string {
	result := make([]rune, len(str))

	for pos, char := range str {
		result[len(str)-pos-1] = char
	}

	return string(result)
}

func getPairs(strings []string) Pairs {
	stringsReversed := []string{}
	for _, str := range strings {
		stringsReversed = append(stringsReversed, reverseString(str))
	}

	trieRoot := buildTrie(strings)
	trieRootReversed := buildTrie(stringsReversed)

	isPalindrome := [][]bool{}
	for _, word := range strings {
		isPalindrome = append(isPalindrome, isPalindromeFrom(word))
	}

	isPalindromeReversed := [][]bool{}
	for _, word := range stringsReversed {
		isPalindromeReversed = append(isPalindromeReversed, isPalindromeFrom(word))
	}

	results := Pairs{}

	for pos, word := range strings {
		for _, palindromeWith := range searchTrie(word, isPalindrome[pos], trieRootReversed) {
			if pos != palindromeWith {
				results = append(results, []int{pos + 1, palindromeWith + 1})
			}
		}
	}

	for pos, word := range stringsReversed {
		for _, palindromeWith := range searchTrie(word, isPalindromeReversed[pos], trieRoot) {
			if pos != palindromeWith {
				results = append(results, []int{palindromeWith + 1, pos + 1})
			}
		}
	}

	sort.Sort(results)

	resultsFiltered := Pairs{}

	prevResult := []int{-1, -1}

	for _, result := range results {
		if !(result[0] == prevResult[0] && result[1] == prevResult[1]) {
			resultsFiltered = append(resultsFiltered, result)
			prevResult = result
		}
	}

	return resultsFiltered
}

func getNumberOfWords() int {
	var numWords int

	fmt.Scanf("%d", &numWords)

	return numWords
}

func getWord() string {
	var word string
	fmt.Scanf("%s\n", &word)
	return word
}

func main() {
	/*
		fmt.Println(buildTrie([]string{"bba"}))
		fmt.Println(isPalindromeFrom("bbabbbb"))
		trieNode := buildTrie([]string{"test", "xxx", "bba", "yyy", "bbab"})

		fmt.Println(reverseString("test"))
		fmt.Println(searchTrie("bbabbbb", isPalindromeFrom("bbabbbb"), trieNode))

		strings := []string{"a", "abbaa", "bba", "abb"}
		fmt.Println(getPairs(strings))
	*/

	numWords := getNumberOfWords()
	words := []string{}

	for range make([]bool, numWords) {
		words = append(words, getWord())
	}

	for _, pair := range getPairs(words) {
		fmt.Println(pair[0], pair[1])
	}
}
