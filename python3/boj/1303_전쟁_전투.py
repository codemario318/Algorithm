'''
전쟁 - 전투 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	2308	908	769	39.375%
문제
전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다.

그러나 당신의 병사들은 하얀 옷을 입고, 적국의 병사들은 파란옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다.

문제는, 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.

N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

입력
첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. (B는 파랑, W는 흰색이다.)

출력
첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.

예제 입력 1 
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
예제 출력 1 
130 65
출처
문제의 오타를 찾은 사람: bluepuha
빠진 조건을 찾은 사람: veydpz, vjerksen
문제를 만든 사람: xhark
'''
from sys import stdin
from collections import deque
from functools import reduce

readline = stdin.readline
OFFSET = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def search(field, M, N, x, y, visited):
    q = deque([(x, y)])

    visited[x][y] = True
    c = feild[x][y]

    cnt = 1

    while q:
        i, j = q.popleft()

        for wi, wj in OFFSET:
            ni, nj = i+wi, j+wj
            if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and c == field[ni][nj]:
                visited[ni][nj] = True
                cnt += 1
                q.append((ni, nj))

    return cnt


if __name__ == '__main__':
    N, M = map(int, readline().split())

    feild = [stdin.readline().strip() for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]

    W, B = [], []

    for i in range(M):
        for j in range(N):
            if visited[i][j]:
                continue
            temp = search(feild, M, N, i, j, visited)

            if feild[i][j] == 'W':
                W.append(temp)
            else:
                B.append(temp)

    w = reduce(lambda prev, cur: prev + (cur**2), W, 0)
    b = reduce(lambda prev, cur: prev + (cur**2), B, 0)
    print(w, b)
