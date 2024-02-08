package leetcode

const PUSH string = "Push"
const POP string = "Pop"

func buildArray(target []int, n int) []string {
	result := make([]string, 0)
	num := 1

	for _, t := range target {
		for num < t {
			result = append(result, PUSH, POP)
			num += 1
		}

		if num == t {
			result = append(result, PUSH)
			continue
		}
	}

	return result
}
