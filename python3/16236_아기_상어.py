'''
아기 상어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	78892	37661	23193	44.421%
문제
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.

둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
아기 상어는 공간에 한 마리 있다.

출력
첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.
'''
from heapq import heappop, heappush
from sys import stdin

readline = stdin.readline

BABY_SHARK = 9
INIT_SIZE = 2
OFFSET = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(board, pos, size):
    length = len(board)
    queue = [(0, pos)]
    visited = {pos}
    min_step = float('inf')

    while queue:
        step, (i, j) = heappop(queue)

        if 0 < board[i][j] < size:
            return step, i, j

        for wi, wj in OFFSET:
            nxt = ni, nj = i + wi, j + wj

            if 0 <= ni < length and 0 <= nj < length and nxt not in visited and board[ni][nj] <= size:
                visited.add(nxt)
                heappush(queue, (step + 1, nxt))

    return min_step, -1, -1


def get_shark_pos(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == BABY_SHARK:
                return i, j

    return -1, -1


if __name__ == '__main__':
    N = int(readline())
    board = [list(map(int, readline().split())) for _ in range(N)]

    shark_pos = si, sj = get_shark_pos(board)
    board[si][sj] = 0

    shark_size = INIT_SIZE
    fish_count = 0
    total_time = 0

    while True:
        time, i, j = bfs(board, shark_pos, shark_size)

        if time == float('inf'):
            break

        board[i][j] = 0
        fish_count += 1

        if fish_count == shark_size:
            fish_count = 0
            shark_size += 1

        shark_pos = (i, j)
        total_time += time

    print(total_time)
