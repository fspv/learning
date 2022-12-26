package main

func canJump(nums []int) bool {
	lastReachable := 0

	for pos, num := range nums {
		if pos <= lastReachable {
			if pos+num > lastReachable {
				lastReachable = pos + num
			}
		} else {
			return false
		}
	}
	return true
}
