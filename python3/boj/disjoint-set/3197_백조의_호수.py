'''
백조의 호수 실패다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	42627	8900	5557	19.535%
문제
두 마리의 백조가 호수에서 살고 있었다. 그렇지만 두 마리는 호수를 덮고 있는 빙판으로 만나지 못한다.

호수는 행이 R개, 열이 C개인 직사각형 모양이다. 어떤 칸은 얼음으로 덮여있다.

호수는 차례로 녹는데, 매일 물 공간과 접촉한 모든 빙판 공간은 녹는다. 두 개의 공간이 접촉하려면 가로나 세로로 닿아 있는 것만 (대각선은 고려하지 않는다) 생각한다.

아래에는 세 가지 예가 있다.

...XXXXXX..XX.XXX ....XXXX.......XX .....XX..........
....XXXXXXXXX.XXX .....XXXX..X..... ......X..........
...XXXXXXXXXXXX.. ....XXX..XXXX.... .....X.....X.....
..XXXXX..XXXXXX.. ...XXX....XXXX... ....X......XX....
.XXXXXX..XXXXXX.. ..XXXX....XXXX... ...XX......XX....
XXXXXXX...XXXX... ..XXXX.....XX.... ....X............
..XXXXX...XXX.... ....XX.....X..... .................
....XXXXX.XXX.... .....XX....X..... .................
      처음               첫째 날             둘째 날
백조는 오직 물 공간에서 세로나 가로로만(대각선은 제외한다) 움직일 수 있다.

며칠이 지나야 백조들이 만날 수 있는 지 계산하는 프로그램을 작성하시오.

입력
입력의 첫째 줄에는 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1500.

다음 R개의 줄에는 각각 길이 C의 문자열이 하나씩 주어진다. '.'은 물 공간, 'X'는 빙판 공간, 'L'은 백조가 있는 공간으로 나타낸다.

출력
첫째 줄에 문제에서 주어진 걸리는 날을 출력한다.

예제 입력 1
10 2
.L
..
XX
XX
XX
XX
XX
XX
..
.L
예제 출력 1
3
예제 입력 2
4 11
..XXX...X..
.X.XXX...L.
....XXX..X.
X.L..XXX...
예제 출력 2
2
예제 입력 3
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
예제 출력 3
2
출처
Olympiad > Croatian Highschool Competitions in Informatics > 2005 > National Competition #2 - Seniors 2번

문제를 번역한 사람: baemin0103
데이터를 추가한 사람: dlbae9613
'''
from collections import deque
from sys import stdin

OFFSET = [(-1, 0), (0, -1), (0, 1), (1, 0)]
WATER = '.'
ICE = 'X'
SWAN = 'L'

readline = stdin.readline


def find(parent, pos):
    i, j = pos

    if parent[i][j] != pos:
        parent[i][j] = find(parent, parent[i][j])

    return parent[i][j]


def union(parent, pos_a, pos_b):
    a, b = find(parent, pos_a), find(parent, pos_b)

    if a != b:
        ai, aj = a
        bi, bj = b

        if a < b:
            parent[bi][bj] = a
        else:
            parent[ai][aj] = b


def is_in_range(board, pos):
    i, j = pos
    return 0 <= i < len(board) and 0 <= j < len(board[0])


def update(lake, parent, melted, cur):
    i, j = cur

    for wi, wj in OFFSET:
        nxt = ni, nj = i + wi, j + wj

        if not is_in_range(lake, nxt):
            continue

        if lake[ni][nj] == WATER:
            union(parent, cur, nxt)
        elif lake[ni][nj] == ICE and nxt not in melted:
            melted.add(nxt)


def init_parent_melted(lake, pos, parent, melted):
    queue = deque([pos])

    while queue:
        i, j = queue.popleft()

        for wi, wj in OFFSET:
            nxt = ni, nj = i + wi, j + wj

            if not is_in_range(lake, nxt):
                continue

            if lake[ni][nj] == ICE:
                melted.add(nxt)
                continue

            if parent[ni][nj] != pos:
                parent[ni][nj] = pos
                queue.append(nxt)


if __name__ == '__main__':
    R, C = map(int, readline().split())
    lake = [list(readline().strip()) for _ in range(R)]

    parent = [[(i, j) for j in range(C)] for i in range(R)]
    melted = set()
    swans = []

    for i in range(R):
        for j in range(C):
            cur = (i, j)

            if lake[i][j] == ICE:
                continue

            if lake[i][j] == SWAN:
                swans.append(cur)

            if parent[i][j] == cur:
                init_parent_melted(lake, cur, parent, melted)

    swan_a, swan_b = swans
    day = 0

    while find(parent, swan_a) != find(parent, swan_b):
        day += 1
        next_melted = set()

        for cur in melted:
            i, j = cur

            lake[i][j] = WATER
            update(lake, parent, next_melted, cur)

        if find(parent, swan_a) == find(parent, swan_b):
            break

        melted = next_melted

    print(day)
