// further: my algorithm is O(n^2), but O(n) is possible
// bucket sort and n_C_2 = n*(n-1)/2
func numIdenticalPairs(nums []int) int {
	gp := 0
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] == nums[j] {
				gp += 1
			}
		}
	}
	return gp
}