// package gymSuit

// func solution(n int, lost []int, reserve []int) int {
// 	newReserve := make([]int, 0)
// 	newLost := make([]int, 0)

// 	for _, r := range reserve {
// 		flg := true
// 		for _, l := range lost {
// 			if r == l {
// 				flg = false
// 				break
// 			}
// 		}

// 		if flg {
// 			newReserve = append(newReserve, r)
// 		} else {
// 			newLost = append(newLost, r)
// 		}
// 	}
// 	return 0
// }