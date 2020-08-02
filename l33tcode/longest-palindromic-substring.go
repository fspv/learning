package main

func longestPalindrome(s string) string {
	dp := [][]bool{}

	for _ = range s {
		dp = append(dp, make([]bool, len(s)))
	}

	maxPalindromeLen, maxPalindromLeft, maxPalindromeRight := 0, 0, -1

	for left := len(s) - 1; left >= 0; left-- {
		for right := left; right < len(s); right++ {
			if left == right {
				dp[left][right] = true
			} else if left+1 == right {
				dp[left][right] = s[left] == s[right]
			} else {
				dp[left][right] = dp[left+1][right-1] && s[left] == s[right]
			}

			if dp[left][right] && right-left+1 > maxPalindromeLen {
				maxPalindromeLen = right - left + 1
				maxPalindromLeft, maxPalindromeRight = left, right
			}
		}
	}

	return s[maxPalindromLeft : maxPalindromeRight+1]
}

func longestPalindromeTopDown(s string) string {
	var isPalindrome func(start, end int) bool
	isPalindrome = func(start, end int) bool {
		if start >= end {
			return true
		}
		if s[start] == s[end] {
			return isPalindrome(start+1, end-1)
		} else {
			return false
		}
	}

	maxPalindromeLen, maxPalindromLeft, maxPalindromeRight := 0, 0, 0

	cache := []map[int]bool{}

	for _ = range s {
		cache = append(cache, map[int]bool{})
	}

	for left := range s {
		for right := left; right < len(s); right++ {
			palindrome := false
			if val, ok := cache[left][right]; ok {
				palindrome = val
			} else {
				palindrome = isPalindrome(left, right)
				cache[left][right] = palindrome
			}
			if palindrome && right-left+1 > maxPalindromeLen {
				maxPalindromeLen = right - left + 1
				maxPalindromLeft, maxPalindromeRight = left, right
			}
		}
	}

	if len(s) == 0 {
		return ""
	}

	return s[maxPalindromLeft : maxPalindromeRight+1]
}
