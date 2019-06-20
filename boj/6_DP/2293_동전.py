'''
동전 1
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	4 MB	21215	8660	6393	41.643%
문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다.
이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다.
경우의 수는 2^31보다 작다.

예제 입력 1
3 10
1
2
5

예제 출력 1
10
출처
어색한 표현을 찾은 사람: dbfldkfdbgml
빠진 조건을 찾은 사람: goodcrane3
데이터를 추가한 사람: jh05013
'''
# from sys import stdin
import time
# from math import *
start = time.time()
# input = lambda: stdin.readline()
#
# n,k = map(int,input().split())
# dp = [0 for _ in range(k+1)]
# dp[0] = 1
#
# for _ in range(n):
#     coin = int(input())
#     for i in range(k-coin+1):
#         dp[coin+i] += dp[i]
#
# print(dp[k])
# print(time.time()-start)
################################################################################
# list(range(-100+1))
# from sys import stdin
#
# n,k = map(int,stdin.readline().split())
# nums = {}
#
# for _ in range(1,n+1):
#     coin = int(stdin.readline())
#     if coin > k: continue
#     try:
#         nums[coin] += 1
#     except KeyError:
#         nums[coin] = 1
#     for i in range(0,k-coin+1):
#         try:
#             nums[coin+i] += nums[i]
#         except KeyError:
#             nums[coin+i] = nums[i]
# try:
#     print(nums[k])
# except KeyError:
#     print(0)

################################################################################

from sys import stdin

def dp(coins,k) :
    counts = [1]+[0 for _ in range(k)]
    for coin in coins:
        for i in range(coin, len(counts)) :
            counts[i] += counts[i-coin]
    return counts[k]

n,k = map(int,stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(n)]

print(dp(coins,k))

# print(time.time()-start)
