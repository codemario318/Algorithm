'''
불! 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	79137	18147	11855	21.027%
문제
지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!

미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.

지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.

불은 각 지점에서 네 방향으로 확산된다.

지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.

지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

입력
입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.

다음 입력으로 R줄동안 각각의 미로 행이 주어진다.

각각의 문자들은 다음을 뜻한다.

#: 벽
.: 지나갈 수 있는 공간
J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
F: 불이 난 공간
J는 입력에서 하나만 주어진다.

출력
지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.

지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.

예제 입력 1
4 4
####
#JF#
#..#
#..#
예제 출력 1
3
출처


Contest > Waterloo's local Programming Contests > 13 June, 2009 B번

문제의 오타를 찾은 사람: apjw6112, vl0612
데이터를 추가한 사람: chayhyeon, dldmswp3, duno72, ktyong1225, myyh1234, pill27211
잘못된 번역을 찾은 사람: jh05013
문제를 번역한 사람: lyzqm
'''
from collections import deque
from sys import stdin

readline = stdin.readline

JIHUN = 'J'
FIRE = 'F'
EMPTY = '.'
WALL = '#'
OFFSET = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_jihun(board):
    for i in range(len(board)):
        for j in range(len(board[-1])):
            if board[i][j] == JIHUN:
                return i, j
    return -1, -1


def find_fires(board):
    fires = []
    for i in range(len(board)):
        for j in range(len(board[-1])):
            if board[i][j] == FIRE:
                fires.append((i, j))
    return fires


def solution(board):
    pos = find_jihun(board)
    jihun_queue = deque([(pos, 0)])
    fire_queue = deque(find_fires(board))

    min_step = float('inf')

    while jihun_queue:
        for _ in range(len(jihun_queue)):
            cur, step = jihun_queue.popleft()
            i, j = cur

            if board[i][j] == FIRE:
                continue

            for wi, wj in OFFSET:
                nxt = (ni, nj) = (i + wi, j + wj)

                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    if board[ni][nj] == EMPTY:
                        jihun_queue.append((nxt, step + 1))
                        board[ni][nj] = JIHUN
                else:
                    min_step = min(min_step, step + 1)

        for _ in range(len(fire_queue)):
            i, j = fire_queue.popleft()
            for wi, wj in OFFSET:
                nxt = (ni, nj) = (i + wi, j + wj)
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (
                        board[ni][nj] == EMPTY or board[ni][nj] == JIHUN):
                    board[ni][nj] = FIRE
                    fire_queue.append(nxt)

    return min_step


if __name__ == '__main__':
    R, C = map(int, readline().split())
    board = [list(readline().rstrip()) for _ in range(R)]

    result = solution(board)

    if result == float('inf'):
        print('IMPOSSIBLE')
    else:
        print(result)
