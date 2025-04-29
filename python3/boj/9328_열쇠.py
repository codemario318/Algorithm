'''
열쇠 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	25775	7817	5376	27.511%
문제
상근이는 1층 빌딩에 침입해 매우 중요한 문서를 훔쳐오려고 한다. 상근이가 가지고 있는 평면도에는 문서의 위치가 모두 나타나 있다. 빌딩의 문은 모두 잠겨있기 때문에, 문을 열려면 열쇠가 필요하다. 상근이는 일부 열쇠를 이미 가지고 있고, 일부 열쇠는 빌딩의 바닥에 놓여져 있다. 상근이는 상하좌우로만 이동할 수 있다.

상근이가 훔칠 수 있는 문서의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 수는 100개를 넘지 않는다.

각 테스트 케이스의 첫째 줄에는 지도의 높이와 너비 h와 w (2 ≤ h, w ≤ 100)가 주어진다. 다음 h개 줄에는 빌딩을 나타내는 w개의 문자가 주어지며, 각 문자는 다음 중 하나이다.

'.'는 빈 공간을 나타낸다.
'*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없다.
'$'는 상근이가 훔쳐야하는 문서이다.
알파벳 대문자는 문을 나타낸다.
알파벳 소문자는 열쇠를 나타내며, 그 문자의 대문자인 모든 문을 열 수 있다.
마지막 줄에는 상근이가 이미 가지고 있는 열쇠가 공백없이 주어진다. 만약, 열쇠를 하나도 가지고 있지 않는 경우에는 "0"이 주어진다.

상근이는 처음에는 빌딩의 밖에 있으며, 빌딩 가장자리의 벽이 아닌 곳을 통해 빌딩 안팎을 드나들 수 있다. 각각의 문에 대해서, 그 문을 열 수 있는 열쇠의 개수는 0개, 1개, 또는 그 이상이고, 각각의 열쇠에 대해서, 그 열쇠로 열 수 있는 문의 개수도 0개, 1개, 또는 그 이상이다. 열쇠는 여러 번 사용할 수 있다.

출력
각 테스트 케이스 마다, 상근이가 훔칠 수 있는 문서의 최대 개수를 출력한다.

예제 입력 1
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony
예제 출력 1
3
1
0
출처


ICPC > Regionals > Europe > Northwestern European Regional Contest > Benelux Algorithm Programming Contest > BAPC 2013 Preliminaries K번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: bamgoesn
문제의 오타를 찾은 사람: goooora, na982, vanila_banana
'''
from collections import deque
from sys import stdin

readline = stdin.readline

OFFSET = [(0, 1), (0, -1), (1, 0), (-1, 0)]

NO_KEY = '0'
EMPTY = '.'
WALL = '*'
TARGET = '$'


def update_mask(mask, key):
    key_index = ord(key) - ord('a')
    return mask | (1 << key_index)


def init_mask(keys):
    mask = 0

    for key in keys:
        mask = update_mask(mask, key)

    return mask


def get_start_positions(h, w):
    return [(i, j) for i in range(h) for j in range(w) if i == 0 or i == w - 1 or j == 0 or j == h - 1]


def is_door(value):
    return 'A' <= value <= 'Z'


def is_key(value):
    return 'a' <= value <= 'z'


def has_key(mask, door):
    door_index = ord(door) - ord('A')
    return mask & (1 << door_index)


def solution(board, h, w, keys):
    visited = [[set() for _ in range(w)] for _ in range(h)]
    mask = init_mask(keys)
    queue = deque(map(lambda pos: (pos, mask), get_start_positions(h, w)))

    for (i, j), mask in queue:
        visited[i][j].add(mask)

    documents = 0

    while queue:
        (i, j), mask = queue.popleft()

        if board[i][j] == TARGET:
            documents += 1
            board[i][j] = EMPTY

        for wi, wj in OFFSET:
            nxt = ni, nj = i + wi, j + wj

            if 0 > ni or ni >= h or 0 > nj or nj >= w:
                continue

            if board[ni][nj] == WALL:
                continue

            if is_door(board[ni][nj]) and not has_key(mask, board[ni][nj]):
                continue

            new_mask = mask

            if is_key(board[ni][nj]):
                new_mask = update_mask(mask, board[ni][nj])

            if new_mask not in visited[ni][nj]:
                visited[ni][nj].add(new_mask)
                queue.append((nxt, new_mask))

    return documents


if __name__ == '__main__':
    T = int(readline())

    for _ in range(T):
        h, w = map(int, readline().split())
        board = [
            [EMPTY for _ in range(w + 2)],
            *[[EMPTY, *readline().rstrip(), EMPTY] for _ in range(h)],
            [EMPTY for _ in range(w + 2)]
        ]
        key_string = readline().rstrip()
        keys = [] if key_string == NO_KEY else list(key_string)

        print(solution(board, h + 2, w + 2, keys))
