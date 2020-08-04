package main

func isPowerOfFour(num int) bool {
	return num > 0 && ((num^(num-1))&num) == num && (num & 0xAAAAAAAA) == 0
}
