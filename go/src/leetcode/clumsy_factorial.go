package leetcode

func clumsy(n int) int {
	opers := []string{"*", "/", "+", "-"}
	idx := 0
	nums := make([]int, n-1)

	for i := n - 1; i > 0; i-- {
		switch opers[idx] {
		case "*":
			nums[len(nums)-1] *= i
		case "/":
			nums[len(nums)-1] /= i
		case "+":
			nums = append(nums, i)
		case "-":
			nums = append(nums, -i)
		}
		idx += 1
	}

	total := 0

	for _, v := range nums {
		total += v
	}

	return total
}
