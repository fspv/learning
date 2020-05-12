func singleNonDuplicate(nums []int) int {
    for pos, _ := range make([]int, len(nums) / 2 + 1) {
        if ((pos * 2 + 1) < len(nums) && nums[pos * 2] != nums[pos * 2 + 1]) || (pos * 2 + 1) == len(nums) {
            return nums[pos * 2]
        }
    }
    return 0
}
