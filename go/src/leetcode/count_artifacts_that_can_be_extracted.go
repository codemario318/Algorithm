package leetcode

func digArtifacts(n int, artifacts [][]int, dig [][]int) int {
	grid := [1000][1000]bool{}
	r, c := 0, 0

	for _, d := range dig {
		r, c = d[0], d[1]
		grid[r][c] = true
	}

	result := 0
	r1, c1, r2, c2 := 0, 0, 0, 0
	flag := true

	for _, artifact := range artifacts {
		flag = true
		r1, c1, r2, c2 = artifact[0], artifact[1], artifact[2], artifact[3]

		for i := r1; i <= r2; i++ {
			for j := c1; j <= c2; j++ {
				if !grid[i][j] {
					flag = false
					break
				}
			}

			if !flag {
				break
			}
		}

		if flag {
			result += 1
		}
	}

	return result
}
