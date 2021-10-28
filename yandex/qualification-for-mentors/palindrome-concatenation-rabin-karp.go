/*
Идея: используем алгоритм Рабин-Карпа для вычисления хешей строк. Потом пытаемся найти для каждого префикса слова другое слово, которое является перевернутой версией этого префикса. Если оставшаяся часть (после префикса) также является палиндромом, то мы можем сформировать пару.
Также можно использовать для этого префиксное дерево (в соседнем файле лежит его имплементация), но почему-то на практике оно оказалось медленней (видимо свойство входных данных).

Сложность:
* Вычисление хеша для каждой строки O(M) по времени, где M - суммарное количество букв. O(N) по памяти, где N - количество слов
* Поиск пар: O(M * N) по времени - для каждого префикса (считай для каждой буквы) мы получаем до N матчей. Если учитывать возможные коллизии, то на каждый матч нам надо запустить проверку на совпадение строк. В этом случае худший случая будет, что мы запускаем проверку каждый раз, то есть оценка по времени увеличивается до O(M^2 * N)
* В конце все результаты надо отсортировать. В худшем случае у нас выходит N^2 резульататов. Отсортировать их займет O(N^2 log N)
* Итоговая оценка по времени будет: O(M^2 * N + N^2 log N)
* По памяти: O(N) - столько нужно, чтобы хеши всех слов
*/
package main

import "fmt"
import "sort"
import "bufio"
import "os"

// Initialize faster IO. Otherwise the solution runs into TLE
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }

// Helper methods
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

func manacher(word string, leftOffset int) []bool {
	/*
		Method for O(n) calculation of all the palindromes in the sting
		https://en.wikipedia.org/wiki/Longest_palindromic_substring
	*/
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
	/*
		Given a word calculated an array indicating if there
		is a palindrome starting from a given position till
		the end of the word
	*/
	notShifted := manacher(word, 0)
	shiftedByOne := manacher(word, 1)

	result := make([]bool, len(word))

	for pos, _ := range word {
		result[pos] = notShifted[pos] || shiftedByOne[pos]
	}

	result = append(result, true)

	return result
}

func buildHashMap(strings []string, alphabetSize int) map[int][]int {
	/*
		Build a Rabin Karp hash map with hashes of all the strings
	*/
	hashMap := map[int][]int{}

	for wordPos, word := range strings {
		hash := 1

		// Rabin-Karp hash calculation
		for _, char := range word {
			hash *= alphabetSize
			hash += int(char - 'a')
		}

		if _, ok := hashMap[hash]; !ok {
			hashMap[hash] = []int{}
		}

		hashMap[hash] = append(hashMap[hash], wordPos)
	}

	return hashMap
}

func searchHashMap(words []string, word string, isPalindrome []bool, hashMap map[int][]int, alphabetSize int) []int {
	/*
		Try to find all the strings in words matching all the possible prefixes
		of a given word. If such a sting found, check if the rest of the word is
		a palindrome, in which case add it to array and return the array in the end
	*/
	hash := 1
	result := []int{}

	for pos, char := range word {
		// Rabin-Karp hash calculation for a prefix
		hash *= alphabetSize
		hash += int(char - 'a')
		if val, ok := hashMap[hash]; ok {
			for _, index := range val {
				// Also need to check for collisions here caused by int overflow
				if isPalindrome[pos+1] && words[index] == word[:pos+1] {
					result = append(result, index)
				}
			}
		}
	}

	return result
}

func reverseString(str string) string {
	/*
		Just a helper method to reverse a given string
	*/
	result := make([]rune, len(str))

	for pos, char := range str {
		result[len(str)-pos-1] = char
	}

	return string(result)
}

func getPairs(strings []string) Pairs {
	/*
		Core of the algorithm. Find all the string pairs, forming a palindrome
		should they be concatenated
	*/
	alphabetSize := getAlphabetSize(strings)

	// Special case. If all the strings consist of just one letter, every
	// two of them can form a palindrome
	if alphabetSize == 1 {
		for left := 0; left < len(strings); left++ {
			for right := 0; right < len(strings); right++ {
				if left != right {
					printf("%d %d\n", left+1, right+1)
				}
			}
		}

		return [][]int{}
	}

	// Just initialize some helper variables here
	stringsReversed := []string{}
	for _, str := range strings {
		stringsReversed = append(stringsReversed, reverseString(str))
	}

	hashMap := buildHashMap(strings, alphabetSize)
	hashMapReversed := buildHashMap(stringsReversed, alphabetSize)

	isPalindrome := [][]bool{}
	for _, word := range strings {
		isPalindrome = append(isPalindrome, isPalindromeFrom(word))
	}

	isPalindromeReversed := [][]bool{}
	for _, word := range stringsReversed {
		isPalindromeReversed = append(isPalindromeReversed, isPalindromeFrom(word))
	}

	results := Pairs{}

	// Search for a strings which a reversed version of a prefix of a given string
	// and where the rest of the string (after the prefix) is a palindrome as well.
	// In such case those two strings once concatenated will form a palindrome
	for pos, word := range strings {
		for _, palindromeWith := range searchHashMap(stringsReversed, word, isPalindrome[pos], hashMapReversed, alphabetSize) {
			if pos != palindromeWith {
				results = append(results, []int{pos + 1, palindromeWith + 1})
			}
		}
	}

	// The same but in another direction. Search prefix of reversed version of the string
	// among initial versions of the strings
	for pos, word := range stringsReversed {
		for _, palindromeWith := range searchHashMap(strings, word, isPalindromeReversed[pos], hashMap, alphabetSize) {
			if pos != palindromeWith {
				results = append(results, []int{palindromeWith + 1, pos + 1})
			}
		}
	}

	// Prepare the output
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

func getAlphabetSize(words []string) int {
	/*
		Get the number of characters used
	*/
	chars := make([]bool, 26)

	for pos, _ := range chars {
		chars[pos] = false
	}

	for _, word := range words {
		for _, char := range word {
			chars[int(char-'a')] = true
		}
	}

	count := 0

	for _, exist := range chars {
		if exist {
			count += 1
		}
	}

	return count
}

func main() {
	defer writer.Flush()

	var numWords int
	scanf("%d\n", &numWords)
	words := []string{}

	for range make([]bool, numWords) {
		var word string
		scanf("%s\n", &word)
		words = append(words, word)
	}

	for _, pair := range getPairs(words) {
		printf("%d %d\n", pair[0], pair[1])
	}
}
