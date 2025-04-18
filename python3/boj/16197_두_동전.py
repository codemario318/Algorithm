'''
두 동전

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	12756	5588	3810	41.772%
문제
N×M 크기의 보드와 4개의 버튼으로 이루어진 게임이 있다. 보드는 1×1크기의 정사각형 칸으로 나누어져 있고, 각각의 칸은 비어있거나, 벽이다. 두 개의 빈 칸에는 동전이 하나씩 놓여져 있고, 두 동전의 위치는 다르다.

버튼은 "왼쪽", "오른쪽", "위", "아래"와 같이 4가지가 있다. 버튼을 누르면 두 동전이 버튼에 쓰여 있는 방향으로 동시에 이동하게 된다.

동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 20)

둘째 줄부터 N개의 줄에는 보드의 상태가 주어진다.

o: 동전
.: 빈 칸
#: 벽
동전의 개수는 항상 2개이다.

출력
첫째 줄에 두 동전 중 하나만 보드에서 떨어뜨리기 위해 눌러야 하는 버튼의 최소 횟수를 출력한다. 만약, 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면, -1을 출력한다.

예제 입력 1
1 2
oo
예제 출력 1
1
예제 입력 2
6 2
.#
.#
.#
o#
o#
##
예제 출력 2
4
예제 입력 3
6 2
..
..
..
o#
o#
##
예제 출력 3
3
예제 입력 4
5 3
###
.o.
###
.o.
###
예제 출력 4
-1
예제 입력 5
5 3
###
.o.
#.#
.o.
###
예제 출력 5
3
출처
문제를 번역한 사람: baekjoon

4 6
######
#o....
#o....
######

6
'''
from collections import deque
from sys import stdin

readline = stdin.readline
OFFSET = [(0, 1), (0, -1), (1, 0), (-1, 0)]
COIN = 'o'
WALL = '#'
LIMIT = 10

def find_coins(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board[-1])) if board[i][j] == COIN]


def drop_coin(board, pos):
    i, j = pos
    return i < 0 or i >= len(board) or j < 0 or j >= len(board[-1])


def get_next(board, pos, offset):
    i, j = pos[0] + offset[0], pos[1] + offset[1]

    if not drop_coin(board, (i, j)) and board[i][j] == WALL:
        return pos

    return i, j


def solution(board):
    a, b, *_ = find_coins(board)
    queue = deque([(a, b, 0)])
    visited = {(a, b)}

    while queue:
        a, b, step = queue.popleft()

        if step >= LIMIT:
            return -1

        if drop_coin(board, a) or drop_coin(board, b):
            return step

        for offset in OFFSET:
            a_next, b_next = get_next(board, a, offset), get_next(board, b, offset)

            if a_next == b_next:
                continue

            if drop_coin(board, a_next) and drop_coin(board, b_next):
                continue

            if (a_next, b_next) in visited:
                continue

            queue.append((a_next, b_next, step + 1))
            visited.add((a_next, b_next))

    return -1


if __name__ == '__main__':
    N, M = map(int, readline().split())
    board = [readline().rstrip() for _ in range(N)]
    print(solution(board))
