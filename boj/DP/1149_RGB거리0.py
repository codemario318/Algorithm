'''
RGB거리
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (언어별 추가 시간 없음)	128 MB	32093	14451	10849	46.445%
문제
RGB거리에 사는 사람들은 집을 빨강, 초록, 파랑중에 하나로 칠하려고 한다.
또한, 그들은 모든 이웃은 같은 색으로 칠할 수 없다는 규칙도 정했다.
집 i의 이웃은 집 i-1과 집 i+1이다.

각 집을 빨강으로 칠할 때 드는 비용, 초록으로 칠할 때 드는 비용, 파랑으로 드는 비용이 주어질 때,
모든 집을 칠할 때 드는 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 수 N이 주어진다. N은 1,000보다 작거나 같다.
둘째 줄부터 N개의 줄에 각 집을 빨강으로 칠할 때, 초록으로 칠할 때, 파랑으로 칠할 때 드는 비용이 주어진다.
비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠할 때 드는 비용의 최솟값을 출력한다.

예제 입력 1
3
26 40 83
49 60 57
13 89 99
예제 출력 1
96
출처
문제를 번역한 사람: baekjoon
빠진 조건을 찾은 사람: djm03178
데이터를 추가한 사람: rdd6584
'''
n=3
costs = [[26, 40, 83],[49, 60, 57],[13, 89, 99]]

n = 4
costs = [[26, 40, 83],[49, 60, 57],[13, 89, 99],[1,1,1]]
from sys import stdin
from copy import deepcopy

n = int(stdin.readline())
costs = [list(map(int, stdin.readline().split())) for _ in range(n)]
cost = costs[0]

for i in range(1,n):
    temp = deepcopy(cost)
    temp[0] = min(cost[1], cost[2]) + costs[i][0]
    temp[1] = min(cost[0], cost[2]) + costs[i][1]
    temp[2] = min(cost[0], cost[1]) + costs[i][2]
    cost = temp

print(min(temp))
