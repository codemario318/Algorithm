package leetcode

import "sort"

func deckRevealedIncreasing(deck []int) []int {
	var result []int

	sort.Ints(deck)

	result = append(result, deck[len(deck)-1])
	deck = deck[:len(deck)-1]

	for len(deck) > 0 {
		last := result[len(result)-1]
		cur := deck[len(deck)-1]

		deck = deck[1:]
		result = append([]int{last, cur}, result[:len(result)-1]...)
	}

	return result
}
