package leetcode

func findLatestStep(arr []int, m int) int {
	binary := make([]rune, len(arr))
	for i := 0; i < len(binary); i++ {
		binary[i] = '0'
	}

	latestSteps := make([]int, len(arr))

	for i, v := range arr {
		binary[v] = '1'
		latestSteps[i] = getLatestBinary(string(binary))
	}

	count := 0

	for _, v := range latestSteps {
		if v == m {
			count += 1
		}
	}

	return count
}

func getLatestBinary(str string) int {
	i := len(str) - 1

	for ; i >= 0; i-- {
		if str[i] == '1' {
			break
		}
	}

	j := i - 1

	for ; j >= 0; j-- {
		if str[j] == '0' {
			break
		}
	}

	return len(str[j+1 : i+1])
}
