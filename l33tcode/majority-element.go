func majorityElement(nums []int) int {
    count := map[int]int{}

    for _, num := range nums {
        count[num] += 1
        if count[num] > len(nums) / 2 {
            return num
        }
    }

    return 0
}
