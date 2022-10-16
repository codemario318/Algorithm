package leetcode

func getWinner(arr []int, k int) int {
	count := 0
	num := 0
	winNum := 0
	a, b := 0, 0

	maxNum := getMaxNum(arr)

	for count < k {
		a, b = arr[0], arr[1]

		if num == maxNum {
			break
		}

		if a > b {
			winNum = a
			arr = getNewArray(arr, a, b)
		} else {
			winNum = b
			arr = getNewArray(arr, b, a)
		}

		if winNum == num {
			count += 1
		} else {
			num = winNum
			count = 1
		}
	}

	return num
}

func getNewArray(arr []int, a int, b int) []int {
	tempArr := make([]int, 0)
	tempArr = append(tempArr, a)
	tempArr = append(tempArr, arr[2:]...)
	tempArr = append(tempArr, b)
	return tempArr
}

func getMaxNum(arr []int) int {
	maxNum := 0

	for _, v := range arr {
		if maxNum < v {
			maxNum = v
		}
	}

	return maxNum
}
