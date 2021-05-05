'''
나이트의 이동 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	24725	11805	8846	46.986%
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1 
5
28
0
출처
University > Tu-Darmstadt Programming Contest > TUD Contest 2001 3번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: sait2000
문제의 오타를 찾은 사람: sgchoi5
링크
PKU Judge Online
TJU Online Judge
'''
from sys import stdin
from collections import deque

readline = stdin.readline
OFFSET = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
          (2, -1), (1, -2), (2, 1), (1, 2)]


def search(si, sj, di, dj):
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([(si, sj, 0)])

    visited[si][sj] = True

    while q:
        i, j, step = q.popleft()

        if i == di and j == dj:
            return step

        for wi, wj in OFFSET:
            ni, nj = i+wi, j+wj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj, step+1))


T = int(readline())

for _ in range(T):
    N = int(readline())
    si, sj = map(int, readline().split())
    di, dj = map(int, readline().split())
    print(search(si, sj, di, dj))
