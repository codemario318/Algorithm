package leetcode

import "fmt"

func main() {
	fmt.Println("start")
	// fmt.Println(spiralMatrixIII(1, 4, 0, 0))
	// fmt.Println(spiralMatrixIII(5, 6, 1, 4))
	fmt.Println(spiralMatrixIII(3, 3, 2, 0))
}

func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {
	var result [][]int
	var visited [102][102]bool

	offset := [4][2]int{
		{-1, 0},
		{0, 1},
		{1, 0},
		{0, -1},
	}

	offsetIdx := 0
	row, col := rStart+1, cStart+1

	result = append(result, []int{rStart, cStart})
	visited[row][col] = true

	for len(result) < rows*cols {
		turnOffsetIdx := turnRight(offsetIdx)
		turnRowWeight, turnColWeight := offset[turnOffsetIdx][0], offset[turnOffsetIdx][1]
		turnRow, turnCol := row+turnRowWeight, col+turnColWeight

		if isInMatrix(rows, cols, turnRow, turnCol) && !visited[turnRow][turnCol] {
			row, col = turnRow, turnCol

			if !isBorder(rows, cols, row, col) {
				visited[row][col] = true
				result = append(result, []int{row - 1, col - 1})
			}

			offsetIdx = turnOffsetIdx
			continue
		}

		rowWeight, colWeight := offset[offsetIdx][0], offset[offsetIdx][1]
		row, col = row+rowWeight, col+colWeight

		if !isBorder(rows, cols, row, col) {
			visited[row][col] = true
			result = append(result, []int{row - 1, col - 1})
		}
	}

	return result
}

func turnRight(offsetIdx int) int {
	return (offsetIdx + 1) % 4
}

func isInMatrix(rows int, cols int, r int, c int) bool {
	return r >= 0 && c >= 0 && r < rows+2 && c < cols+2
}

func isBorder(rows int, cols int, r int, c int) bool {
	return r == 0 || c == 0 || r == rows+1 || c == cols+1
}
