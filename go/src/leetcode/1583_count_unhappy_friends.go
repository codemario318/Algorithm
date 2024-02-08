package leetcode

func unhappyFriends(n int, preferences [][]int, pairs [][]int) int {
	count := 0
	newPairs := getPairs(n, pairs)
	newPreferences := getPreferences(preferences)

	for target := 0; target < n; target++ {
		targetPair := newPairs[target]
		targetBest := preferences[target][0]

		if targetPair == targetBest {
			continue
		}

		targetBestPair := newPairs[targetBest]

		levelOfTargetBestAndTarget := newPreferences[targetBest][target]
		levelOfTargetBestAndPair := newPreferences[targetBest][targetBestPair]

		if levelOfTargetBestAndTarget < levelOfTargetBestAndPair {
			count++
		}
	}

	return count
}

func getPairs(n int, pairs [][]int) []int {
	arr := make([]int, n)

	for _, pair := range pairs {
		arr[pair[0]] = pair[1]
		arr[pair[1]] = pair[0]
	}

	return arr
}

func getPreferences(preferences [][]int) map[int]map[int]int {
	newPreferences := make(map[int]map[int]int)

	for target, levels := range preferences {
		newPreferences[target] = make(map[int]int)
		for level, friend := range levels {
			newPreferences[target][friend] = level
		}
	}

	return newPreferences
}

func getPreferenceLevel(preferences [][]int, my int, target int) int {
	level := 0
	for lv, friend := range preferences[my] {
		if friend == target {
			level = lv
		}
	}
	return level
}
