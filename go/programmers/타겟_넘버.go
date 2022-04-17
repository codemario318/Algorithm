package targetNumber

func solution(numbers []int, target int) int {
	visited := make([]bool, len(numbers))

	result := dfs(numbers, target, 0, 0, visited)

	return result
}

func dfs(numbers []int, target int, total int, cur int, visited []bool) int {
	if cur == len(numbers) {
		if total == target {
			return 1
		}
		return 0
	}

	visited[cur] = true

	number := numbers[cur]

	minusTotal := total - number
	plusTotal := total + number

	return dfs(numbers, target, minusTotal, cur+1, visited) + dfs(numbers, target, plusTotal, cur+1, visited)
}
