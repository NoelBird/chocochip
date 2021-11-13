// 1480. Running Sum of 1d Array
// it is slow because appended to array

func runningSum(nums []int) []int {
	tmp := []int{}
	cur := 0
	for i := 0; i < len(nums); i++ {
		cur += nums[i]
		tmp = append(tmp, cur)
	}

	return tmp
}