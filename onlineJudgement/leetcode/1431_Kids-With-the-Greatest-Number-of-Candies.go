func kidsWithCandies(candies []int, extraCandies int) []bool {
	// find max value
	var max int = 0
	for i := 0; i < len(candies); i++ {
		if candies[i] > max {
			max = candies[i]
		}
	}
	// subtract max valute to each candies value
	rslt := []bool{}
	for i := 0; i < len(candies); i++ {
		candies[i] += (-max) + extraCandies
		if candies[i] >= 0 {
			rslt = append(rslt, true)
		} else {
			rslt = append(rslt, false)
		}
	}
	return rslt

}