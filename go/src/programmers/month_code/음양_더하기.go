package main

func main() {
	absolutes := []int {4,7,12}
	signs := []bool {true, false, true}

	println(solution(absolutes, signs))
}

func solution(absolutes []int, signs []bool) int {
	result := 0

	for i := 0; i < len(absolutes); i++ {
		absolute := absolutes[i]
		sign := signs[i]

		if sign {
			result += absolute
		} else {
			result += -absolute
		}
	}

	return result
}