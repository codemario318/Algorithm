'''
연구소

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	113274	65923	36920	55.464%
문제
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

예제 입력 1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
예제 출력 1
27
예제 입력 2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
예제 출력 2
9
예제 입력 3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
예제 출력 3
3
출처
문제를 만든 사람: baekjoon
빠진 조건을 찾은 사람: bupjae, dotorya
데이터를 추가한 사람: raboribus

- 모든 빈 공간(0)을 순회한다.
    1. 빈 공간에 벽을 친다. (3개)
        - 바이러스(2)를 감싼다.
            - 바이러스(2) 기준으로 주변 공간 확인 (상, 하, 좌, 우)
        - 벽(1)을 연장 하여 안전 공간을 최대한 확보한다.
            - 벽(1)을 기준으로 막힌 공간 확보(상, 하, 좌, 우, 대각선)
        - 빈 공간(0)에 벽을 세워 새로운 안전 공간을 확보한다.
            - 상, 하, 좌, 우, 대각선
        - 바이러스가 퍼질 공간을 매꿔 안전 공간 확보
        -> 벽은 어느 빈 공간에 적용해야한다는 좋건은 없으므로 예상되는 상황에 대해서 확인하는 것 보다는 모든 경우의 수를 처리하는 것이 더 깔끔할 듯
        -> 백트래킹 적용?
    2. 바이러스를 퍼트린다.
        - 바이러스의 위치에 따라 퍼지는 형태로 bfs로 해도 괜찮을 듯
    3. 안전 구역을 센다.
        - 단순 반복문 가능
- 가장 큰 안전 구역을 저장한다.
'''

from sys import stdin
from collections import deque

SPACE = '0'
WALL = '1'
VIRUS = '2'
STEP = 3
OFFSET = [(0, 1), (0, -1), (-1, 0), (1, 0)]

readline = stdin.readline


def backtracking(board, visited):
    if len(visited) == STEP:
        return count_safe_area(board)

    count = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != SPACE or (i, j) in visited:
                continue

            board[i][j] = WALL
            visited.add((i, j))

            count = max(count, backtracking(board, visited))

            board[i][j] = SPACE
            visited.remove((i, j))

    return count


def count_safe_area(board):
    virus_positions = spread_virus(board)
    count = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == SPACE and (i, j) not in virus_positions:
                count += 1

    return count


def spread_virus(board):
    queue = deque(get_virus_positions(board))
    visited = set(queue)

    while queue:
        i, j = queue.popleft()

        for wi, wj in OFFSET:
            nxt = (ni, nj) = i + wi, j + wj

            if is_in_board(board, nxt) and nxt not in visited and board[ni][nj] == SPACE:
                queue.append(nxt)
                visited.add(nxt)

    return visited


def is_in_board(board, position):
    i, j = position
    return 0 <= i < len(board) and 0 <= j < len(board[0])


def get_virus_positions(board):
    return ((i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == VIRUS)


if __name__ == '__main__':
    N, M = map(int, readline().split())
    board = [readline().split() for _ in range(N)]

    print(backtracking(board, set()))
