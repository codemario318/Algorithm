
stock = 4
dates = [4,10,15]
supplies = [20,5,5]
k = 30
import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    i = 0
    dates.append(k)
    supplies.append(0)
    hq = []
    while stock < k:
        if stock >= dates[i]:
            heapq.heappush(hq,-1*supplies[i])
            i += 1
        else:
            stock += -1 * heapq.heappop(hq)
            answer += 1
    return answer
