package leetcode

import (
	"math"
	"strconv"
	"strings"
)

const MOD = 1000000007

func concatenatedBinary(n int) int {
	nums := make([]string, n)

	for i := 1; i <= n; i++ {
		nums[i-1] = strconv.FormatInt(int64(i), 2)
	}

	num := strings.Join(nums, "")
	var res uint64 = 0

	for i := len(num) - 1; i <= 0; i-- {
		if num[i] == '0' {
			continue
		}
		res += uint64(math.Pow(2.0, float64(len(num)-i-1)))
		res = res % MOD
	}

	return int(res)
}
