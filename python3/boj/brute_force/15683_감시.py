'''
감시 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	20566	9164	5327	40.927%
문제
스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다. 사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.

				
1번	2번	3번	4번	5번
1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.

CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다. CCTV가 감시할 수 없는 영역은 사각지대라고 한다.

CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.

0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다. 위의 예시에서 1번의 방향에 따라 감시할 수 있는 영역을 '#'로 나타내면 아래와 같다.

0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 # 6 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
# # 1 0 6 0
0 0 0 0 0 0
0 0 # 0 0 0
0 0 # 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 # 0 0 0
→	←	↑	↓
CCTV는 벽을 통과할 수 없기 때문에, 1번이 → 방향을 감시하고 있을 때는 6의 오른쪽에 있는 벽을 감시할 수 없다.

0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
위의 예시에서 감시할 수 있는 방향을 알아보면 아래와 같다.

0 0 0 0 0 #
# 2 # # # #
0 0 0 0 6 #
0 6 # # 2 #
0 0 0 0 0 #
# # # # # 5
0 0 0 0 0 #
# 2 # # # #
0 0 0 0 6 #
0 6 0 0 2 #
0 0 0 0 # #
# # # # # 5
0 # 0 0 0 #
0 2 0 0 0 #
0 # 0 0 6 #
0 6 # # 2 #
0 0 0 0 0 #
# # # # # 5
0 # 0 0 0 #
0 2 0 0 0 #
0 # 0 0 6 #
0 6 0 0 2 #
0 0 0 0 # #
# # # # # 5
왼쪽 상단 2: ↔, 오른쪽 하단 2: ↔	왼쪽 상단 2: ↔, 오른쪽 하단 2: ↕	왼쪽 상단 2: ↕, 오른쪽 하단 2: ↔	왼쪽 상단 2: ↕, 오른쪽 하단 2: ↕
CCTV는 CCTV를 통과할 수 있다. 아래 예시를 보자.

0 0 2 0 3
0 6 0 0 0
0 0 6 6 0
0 0 0 0 0
위와 같은 경우에 2의 방향이 ↕ 3의 방향이 ←와 ↓인 경우 감시받는 영역은 다음과 같다.

# # 2 # 3
0 6 # 0 #
0 0 6 6 #
0 0 0 0 #
사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

CCTV의 최대 개수는 8개를 넘지 않는다.

출력
첫째 줄에 사각 지대의 최소 크기를 출력한다.

예제 입력 1 
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
예제 출력 1 
20
예제 입력 2 
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
예제 출력 2 
15
예제 입력 3 
6 6
1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1
예제 출력 3 
6
예제 입력 4 
6 6
1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 5 0 0
0 0 5 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1
예제 출력 4 
2
예제 입력 5 
1 7
0 1 2 3 4 5 6
예제 출력 5 
0
예제 입력 6 
3 7
4 0 0 0 0 0 0
0 0 0 2 0 0 0
0 0 0 0 0 0 4
예제 출력 6 
0
출처
문제를 만든 사람: baekjoon
'''
from sys import stdin
from copy import deepcopy


def readline(): return stdin.readline().split()


def up(board, i, j, visited):
    for k in range(i-1, -1, -1):
        if board[k][j] == '6':
            break
        elif board[k][j] == '0':
            visited.add((k, j))


def down(board, i, j, visited):
    h = len(board)

    for k in range(i+1, h):
        if board[k][j] == '6':
            break
        elif board[k][j] == '0':
            visited.add((k, j))


def left(board, i, j, visited):
    for k in range(j-1, -1, -1):
        if board[i][k] == '6':
            break
        elif board[i][k] == '0':
            visited.add((i, k))


def right(board, i, j, visited):
    w = len(board[0])

    for k in range(j+1, w):
        if board[i][k] == '6':
            break
        elif board[i][k] == '0':
            visited.add((i, k))


def watch(board, sight, i, j, visited):
    for angle in sight:
        angle(board, i, j, visited)


def getBlack(board):
    return sum(map(lambda x: x.count('0'), board))


CAM_ANGLES = {
    '1': [[up], [down], [left], [right]],
    '2': [[up, down], [left, right]],
    '3': [[up, right], [up, left], [down, left], [down, right]],
    '4': [[left, up, right], [up, right, down], [right, down, left], [down, left, up]],
    '5': [[up, down, left, right]]
}


def search(board, cams, step, visited):
    if len(cams) == step:
        return len(visited)

    black = 0
    i, j = cams[step]
    cam = board[i][j]

    for sight in CAM_ANGLES[cam]:
        nextBoard = deepcopy(board)
        nextVisited = deepcopy(visited)
        watch(nextBoard, sight, i, j, nextVisited)
        black = max(black, search(nextBoard, cams, step+1, nextVisited))

    return black


if __name__ == "__main__":
    N, _ = map(int, readline())
    board = []
    cams = []
    blackNum = 0

    for i in range(N):
        line = []
        for j, item in enumerate(readline()):
            line.append(item)
            if item != '0' and item != '6':
                cams.append((i, j))
            elif item == '0':
                blackNum += 1
        board.append(line)

    print(blackNum - search(board, cams, 0, set()))


'''
from sys import stdin
from copy import deepcopy


def readline(): return stdin.readline().split()


def up(board, i, j):
    for k in range(i-1, -1, -1):
        if board[k][j] == '6':
            break
        elif board[k][j] == '0':
            board[k][j] = '#'


def down(board, i, j):
    h = len(board)

    for k in range(i+1, h):
        if board[k][j] == '6':
            break
        elif board[k][j] == '0':
            board[k][j] = '#'


def left(board, i, j):
    for k in range(j-1, -1, -1):
        if board[i][k] == '6':
            break
        elif board[i][k] == '0':
            board[i][k] = '#'


def right(board, i, j):
    w = len(board[0])

    for k in range(j+1, w):
        if board[i][k] == '6':
            break
        elif board[i][k] == '0':
            board[i][k] = '#'


def watch(board, sight, i, j):
    for angle in sight:
        angle(board, i, j)


def getBlack(board):
    return sum(map(lambda x: x.count('0'), board))


CAM_ANGLES = {
    '1': [[up], [down], [left], [right]],
    '2': [[up, down], [left, right]],
    '3': [[up, right], [up, left], [down, left], [down, right]],
    '4': [[left, up, right], [up, right, down], [right, down, left], [down, left, up]],
    '5': [[up, down, left, right]]
}


def search(board, cams, step):
    if len(cams) == step:
        return getBlack(board)

    black = float('inf')
    i, j = cams[step]
    cam = board[i][j]

    for sight in CAM_ANGLES[cam]:
        nextBoard = deepcopy(board)
        watch(nextBoard, sight, i, j)
        black = min(black, search(nextBoard, cams, step+1))

    return black


if __name__ == "__main__":
    N, _ = map(int, readline())
    board = []
    cams = []

    for i in range(N):
        line = []
        for j, item in enumerate(readline()):
            line.append(item)
            if item != '0' and item != '6':
                cams.append((i, j))
        board.append(line)

    print(search(board, cams, 0))
'''