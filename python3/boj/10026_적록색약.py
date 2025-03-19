'''
적록색약 실패다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	80547	46900	35197	57.007%
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
예제 출력 1
4 3
출처
Olympiad > USA Computing Olympiad > 2013-2014 Season > USACO March 2014 Contest > Bronze 3번

문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: corea
'''
from collections import deque
from sys import stdin

readline = stdin.readline

OFFSET = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(board, pos, visited, target):
    queue = deque([pos])

    while queue:
        i, j = queue.popleft()

        for wi, wj in OFFSET:
            nxt = ni, nj = i + wi, j + wj

            if is_in_board(board, nxt) and not visited[ni][nj] and board[ni][nj] in target:
                visited[ni][nj] = True
                queue.append(nxt)


def is_in_board(board, pos):
    i, j = pos
    return 0 <= i < len(board) and 0 <= j < len(board)


def solution(board, n, target):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] or board[i][j] not in target:
                continue
            visited[i][j] = True
            bfs(board, (i, j), visited, target)
            count += 1

    return count


if __name__ == '__main__':
    N = int(readline())
    board = [readline().rstrip() for _ in range(N)]
    r = solution(board, N, set('R'))
    g = solution(board, N, set('G'))
    b = solution(board, N, set('B'))
    rg = solution(board, N, set('RG'))

    print(r + g + b, b + rg)
