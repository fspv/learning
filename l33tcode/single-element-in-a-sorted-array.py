func singleNonDuplicate(nums []int) int {
    for pos, _ := range make([]int, len(nums) / 2) {
        if nums[pos * 2] != nums[pos * 2 + 1] {
            return nums[pos * 2]
        }
    }
    return nums[len(nums) - 1]
}
