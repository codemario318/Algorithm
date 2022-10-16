package leetcode

import "fmt"

func isRobotBounded(instructions string) bool {
	dist := []int{0, 0, 0, 0}

	idx := 0

	for _, cmd := range instructions {
		switch cmd {
		case 'G':
			dist[idx] += 1
		case 'L':
			idx = (idx + 5) % 4
		case 'R':
			idx = (idx + 1) % 4
		}
	}

	fmt.Println(dist)

	return true
}
