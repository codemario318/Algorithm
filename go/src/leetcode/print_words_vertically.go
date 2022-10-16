package leetcode

import (
	"fmt"
	"strconv"
	"strings"
)

func printVertically(s string) []string {
	words := strings.Split(s, " ")
	maxLen := getMaxLen(words)

	words = getPaddingEmptyString(maxLen, words)
	verticallyWords := getVerticallyWordRunes(maxLen, words)
	return getResult(verticallyWords)
}

func getPaddingEmptyString(maxLen int, words []string) []string {
	format := getPaddingEmptyStringFormat(maxLen)

	for i := 0; i < len(words); i++ {
		words[i] = fmt.Sprintf(format, words[i])
	}

	return words
}

func getPaddingEmptyStringFormat(maxLen int) string {
	stringMaxLen := strconv.FormatInt(int64(maxLen), 10)
	return "%-" + stringMaxLen + "s"
}

func getMaxLen(words []string) int {
	maxLen := 0

	for _, word := range words {
		maxLen = max(maxLen, len(word))
	}

	return maxLen
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func getVerticallyWordRunes(maxLen int, words []string) [][]rune {
	verticallyWords := make([][]rune, maxLen)

	idx := 0

	for _, word := range words {
		for i, c := range word {
			idx = i % maxLen
			verticallyWords[idx] = append(verticallyWords[idx], c)
		}
	}

	return verticallyWords
}

func getResult(verticallyWords [][]rune) []string {
	result := make([]string, len(verticallyWords))

	target := make([]rune, 0)
	j := 0

	for i := 0; i < len(verticallyWords); i++ {
		target = verticallyWords[i]
		j = len(target) - 1

		for j > 0 && target[j] == ' ' {
			j--
		}

		result[i] = string(target[:j+1])
	}

	return result
}
