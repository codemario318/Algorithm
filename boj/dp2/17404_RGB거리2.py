'''
RGB거리 2

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	128 MB	236	119	106	56.989%

문제

RGB거리에 사는 사람들은 집을 빨강, 초록, 파랑중에 하나로 칠하려고 한다.
또한, 그들은 모든 이웃은 같은 색으로 칠할 수 없다는 규칙도 정했다.
집 i의 이웃은 집 i-1과 집 i+1이고, 첫 집과 마지막 집도 이웃이다.

각 집을 빨강으로 칠할 때 드는 비용,
초록으로 칠할 때 드는 비용,
파랑으로 드는 비용이 주어질 때,
모든 집을 칠하는 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 수 N이 주어진다.
N은 1,000보다 작거나 같다.
둘째 줄부터 N개의 줄에 각 집을 빨강으로, 초록으로, 파랑으로 칠하는 비용이 주어진다.
비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

예제 입력 1
3
26 40 83
49 60 57
13 89 99

110

3
1 2 4
32 16 8
128 64 256

73

4
26 40 83
49 60 57
13 89 99
100 100 100

196

4
26 40 83
49 60 57
13 89 99
1 100 100

179

4
1 100 100
1000 3 1000
200 1000 400
1 1000 1000


예제 출력 1
110
출처
문제를 만든 사람: baekjoon
메모
메모 작성하기
'''
from sys import stdin,setrecursionlimit
setrecursionlimit(10000)
nxt = [(1,2),(0,2),(0,1)]

def rgb(n,s,c):
    if n == N:
        return 0 if s != c else float('inf')
    if cache[n][s][c] != -1:
        return cache[n][s][c]
    cache[n][s][c] = min(map(lambda x: rgb(n+1,s,x) + costs[n][x] ,nxt[c]))
    return cache[n][s][c]

N = int(stdin.readline())
costs = [ list(map(int,stdin.readline().split())) for _ in range(N)]
cache = [[[-1 for _ in range(3)] for _ in range(3)] for _ in range(N)]

print(min(map(lambda x: rgb(1,x,x)+ costs[0][x],range(3))))

# print()
# for c in cache:print(c)


# 40+49+89+1
# 40+57+13+100
# 40+57+89+1
# for _ in range(1000):
#     print('1000 1000 1000')
