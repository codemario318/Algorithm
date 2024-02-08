package leetcode

func processQueries(queries []int, m int) []int {
	arr := make([]int, m)

	for i := 0; i < m; i++ {
		arr[i] = i + 1
	}

	for _, query := range queries {
		idx := search(arr, query)
		temp := arr[:idx]
		for i := 0; i < len(temp)-1; i++ {
			temp[i+1] = temp[i]
		}
		arr[0] = query
	}

	return arr
}

func search(arr []int, val int) int {
	for i, v := range arr {
		if v == val {
			return i
		}
	}

	return -1
}
