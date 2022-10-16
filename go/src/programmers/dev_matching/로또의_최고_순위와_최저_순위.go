package main

import "fmt"

const lotto_count int = 6

func main() {
	lottos := []int {44, 1, 0, 0, 31, 25}
	win_nums := []int {31, 10, 45, 1, 6, 19}

	lottos = []int {0, 0, 0, 0, 0, 0,}
	win_nums = []int {38, 19, 20, 40, 15, 25}

	result := solution(lottos, win_nums)
	
	fmt.Printf("%d %d\n", result[0], result[1])
}

func solution(lottos []int, win_nums []int) []int {
	var win_count int
	var cand_count int

	for _, lotto_num := range lottos {
		if lotto_num == 0 {
			cand_count++
			continue
		}

		for _, win_num := range win_nums {
			if lotto_num == win_num {
				win_count++
                break
			}
		}
	}

	result := getRank(win_count, cand_count)

    return result
}

func getRank(win_count int, cand_count int) []int {
	lotto_rank := map[int]int{
		6: 1,
		5: 2,
		4: 3,
		3: 4,
		2: 5,
		1: 6,
		0: 6,
	}
    
	min_win_count := win_count
    min_rank, _ := lotto_rank[min_win_count]

	max_win_count := win_count + cand_count
    max_rank, _ := lotto_rank[max_win_count]

	return []int {max_rank, min_rank}
}