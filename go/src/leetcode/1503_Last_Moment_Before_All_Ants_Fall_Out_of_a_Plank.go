package leetcode

import "math"

func getLastMoment(n int, left []int, right []int) int {
	leftStep := arrMax(left)
	rightStep := n - arrMin(right)
	return max(leftStep, rightStep)
}

func arrMax(arr []int) int {
	maxVal := 0

	for _, v := range arr {
		if maxVal < v {
			maxVal = v
		}
	}

	return maxVal
}

func arrMin(arr []int) int {
	minVal := math.MaxInt32

	for _, v := range arr {
		if minVal > v {
			minVal = v
		}
	}

	return minVal
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
