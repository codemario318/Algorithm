package leetcode

func carPooling(trips [][]int, capacity int) bool {
	memTripPassengers := make([]int, 1001)
	count, from, to := 0, 0, 0

	for _, trip := range trips {
		count, from, to = trip[0], trip[1], trip[2]
		for i := from; i <= to; i++ {
			memTripPassengers[i] += count
		}
	}

	for _, total := range memTripPassengers {
		if capacity < total {
			return false
		}
	}

	return true
}
