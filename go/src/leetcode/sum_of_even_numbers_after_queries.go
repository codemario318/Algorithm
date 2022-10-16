package leetcode

func sumEvenAfterQueries(nums []int, queries [][]int) []int {
	var result []int
	var val int
	var idx int

	for _, query := range queries {
		val, idx = query[0], query[1]

		nums[idx] += val
	
		total := 0

		for _, num := range nums {
			if num % 2 == 0 {
				total += num
			}
		}

		result = append(result, total)
	}

	return result
}