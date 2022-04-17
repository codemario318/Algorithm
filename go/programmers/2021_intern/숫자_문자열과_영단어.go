package main

import "strconv"

func main() {
	s := "one4seveneight"
	s = "1zerotwozero3"
	result := solution(s)
	println(result)
}

func solution(s string) int {
	wordToNum := map[string]string {
		"zero": "0",
		"one": "1",
		"two": "2",
		"three": "3",
		"four": "4",
		"five": "5",
		"six": "6",
		"seven": "7",
		"eight": "8",
		"nine": "9",
		"0": "0",
		"1": "1",
		"2": "2",
		"3": "3",
		"4": "4",
		"5": "5",
		"6": "6",
		"7": "7",
		"8": "6",
		"9": "9",
	}
    
    convertNums := ""
    tempWord := ""

	for _, c := range s {
		tempWord += string(c)

        if num, ok := wordToNum[tempWord]; ok {
			convertNums += num
			tempWord = ""
		}
	}

	result, _ := strconv.Atoi(convertNums)
	return result
}