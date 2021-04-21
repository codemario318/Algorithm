'''
아기 상어 2 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	1491	850	669	55.016%
문제
N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자. 

입력
첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다. 빈 칸의 개수가 한 개 이상인 입력만 주어진다.

출력
첫째 줄에 안전 거리의 최댓값을 출력한다.

예제 입력 1 
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
예제 출력 1 
2
예제 입력 2 
7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1
예제 출력 2 
2
출처
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: jh05013
데이터를 추가한 사람: jyn47
'''
from sys import stdin
from collections import deque

OFFSET = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def readline(): return map(int, stdin.readline().split())


def search(board, N, M):
    sharks = [(i, j, 0) for i in range(N)
              for j in range(M) if board[i][j] == 1]

    q = deque(sharks)
    res = 0

    while q:
        i, j, d = q.popleft()

        if d > res:
            res = d

        for wi, wj in OFFSET:
            ni, nj = i+wi, j+wj
            if 0 <= ni < N and 0 <= nj < M and not board[ni][nj]:
                board[ni][nj] = d+1
                q.append((ni, nj, d+1))

    return res


def main():
    N, M = readline()
    board = [list(readline()) for _ in range(N)]

    res = search(board, N, M)
    print(res)


if __name__ == '__main__':
    main()
