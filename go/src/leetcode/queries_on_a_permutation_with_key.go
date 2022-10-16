package leetcode

func processQueries(queries []int, m int) []int {
	positions := make(map[int]int)
	arr := make([]int, m)

	for i := 0; i < m; i++ {
		arr[i] = i + 1
		positions[i+1] = i
	}

	idx := 0
	for _, query := range queries {
		idx = positions[query]

	}
}
