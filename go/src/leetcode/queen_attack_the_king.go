package leetcode

func queensAttacktheKing(queens [][]int, king []int) [][]int {
	OFFSET := [...][2]int{
		{0, 1},
		{0, -1},
		{1, 0},
		{-1, 0},
		{1, 1},
		{-1, -1},
		{1, -1},
		{-1, 1},
	}
	var board [8][8]bool
	var result [][]int

	kx, ky := king[0], king[1]
	wx, wy := 0, 0
	nx, ny := 0, 0

	for _, queen := range queens {
		a, b := queen[0], queen[1]
		board[a][b] = true
	}

	for _, offset := range OFFSET {
		wx, wy = offset[0], offset[1]
		nx, ny = kx+wx, ky+wy

		for nx <= 0 && ny <= 0 && nx > 8 && ny > 8 {
			if board[nx][ny] == true {
				result = append(result, []int{nx, ny})
				break
			}
		}
	}

	return result
}
