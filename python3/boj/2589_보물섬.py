'''
보물섬

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	51896	19867	14196	38.514%
문제
보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.



예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.



보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.

출력
첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.

예제 입력 1
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
예제 출력 1
8

4 4
LLLL
LLLL
LLLL
LLLL

6

4 4
LLLL
LWWL
LWWL
LLLL

6

4 4
LLLL
LWWW
LWWW
LLLL

9

4 4
LLLL
LWWL
LWWW
LLLL

10

5 9
LLLLLLLLL
LWWWLWWWL
LWWWLWWWL
LWWWLWWWL
LLLLLLLLW

15

출처
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2005 > 초등부 3번

데이터를 추가한 사람: bueno, cseteram, seico75, surung9898
'''
from collections import deque
from sys import stdin

readline = stdin.readline

OFFSET = [(0, 1), (1, 0), (0, -1), (-1, 0)]
LAND = 'L'


def bfs(board, i, j):
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[i][j] = True

    queue = deque([(i, j, 0)])
    max_step = 0

    while queue:
        i, j, step = queue.popleft()

        max_step = max(max_step, step)

        for wi, wj in OFFSET:
            (ni, nj) = i + wi, j + wj

            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == LAND and not visited[ni][nj]:
                visited[ni][nj] = True
                queue.append((ni, nj, step + 1))

    return max_step


if __name__ == '__main__':
    N, M = map(int, readline().split())
    board = [list(readline().rstrip()) for _ in range(N)]

    max_step = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] != LAND:
                continue
            max_step = max(max_step, bfs(board, i, j))

    print(max_step)
