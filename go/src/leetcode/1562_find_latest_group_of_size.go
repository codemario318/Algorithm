package leetcode

import (
	"fmt"
	"math"
)

func findLatestStep(arr []int, m int) int {
	binaries := make([]string, len(arr))

	for i, v := range arr {
		binaries[i] = fmt.Sprintf("%b", v|int(math.Pow(2.0, float64(m))))
	}

	latestSteps := make([]string, len(arr))

	for i, binary := range binaries {
		latestSteps[i] = getLatestBinary(binary)
	}

	fmt.Println(binaries)

	return 0
}

func getLatestBinary(str string) string {
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

	return str[j+1 : i+1]
}
