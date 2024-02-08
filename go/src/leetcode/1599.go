package leetcode

const LIMIT = 4

func minOperationsMaxProfit(customers []int, boardingCost int, runningCost int) int {
	customers = set(customers)
	total := 0
	totalCost := 0
	rotateCount := 0
	count := 0

	if boardingCost*LIMIT <= runningCost {
		return -1
	}

	for i := 0; i < len(customers)-1; i++ {
		count = customers[i]
		totalCost = boardingCost * count
		total += totalCost
		total -= runningCost
		rotateCount += 1
	}

	count = customers[len(customers)-1]
	totalCost = boardingCost * count

	if totalCost > boardingCost {
		total += totalCost
		total -= runningCost
		rotateCount += 1
	}

	if total <= 0 {
		return -1
	}
	return rotateCount
}

func set(customers []int) []int {
	count := 0
	for i := 0; i < len(customers)-1; i++ {
		count = customers[i]
		if count > LIMIT {
			customers[i] = LIMIT
			customers[i+1] += count - LIMIT
		}
	}

	for customers[len(customers)-1] > LIMIT {
		count = customers[len(customers)-1] - LIMIT
		customers[len(customers)-1] = LIMIT
		customers = append(customers, count)
	}
	return customers
}
