func isPowerOfTwo(n int) bool {
    for num := float64(n); num > 0; num /= 2 {
		if num == 1 {
			return true
		}
	}
	return false
}
