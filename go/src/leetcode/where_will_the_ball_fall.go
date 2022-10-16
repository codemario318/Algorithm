package leetcode


func findBall(grid [][]int) []int {
	colOfBalls := make([]int, len(grid[0]))

	for i := 0; i < len(colOfBalls); i++ {
		colOfBalls[i] = i
	}

	colOfBall := 0
	offset := 0

	next := 0

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(colOfBalls); j++ {
			colOfBall = colOfBalls[j]

			if colOfBall == -1 {
				continue
			}

			offset = grid[i][colOfBall]
			next = colOfBall + offset

			if next < 0 || next >= len(grid[0]) || offset != grid[i][next] {
				colOfBalls[j] = -1
			} else {
				colOfBalls[j] = next				
			}
		}
	}

	return colOfBalls
}
