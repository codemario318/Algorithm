'''
달이 차오른다, 가자.

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	20049	8533	5813	39.620%
문제
지금 민식이가 계획한 여행은 달이 맨 처음 뜨기 시작할 때 부터, 준비했던 여행길이다. 하지만, 매번 달이 차오를 때마다 민식이는 어쩔 수 없는 현실의 벽 앞에서 다짐을 포기하고 말았다.

민식이는 매번 자신의 다짐을 말하려고 노력했지만, 말을 하면 아무도 못 알아들을 것만 같아서, 지레 겁먹고 벙어리가 되어버렸다. 결국 민식이는 모두 잠든 새벽 네시 반쯤 홀로 일어나, 창 밖에 떠있는 달을 보았다.

하루밖에 남지 않았다. 달은 내일이면 다 차오른다. 이번이 마지막기회다. 이걸 놓치면 영영 못간다.

영식이는 민식이가 오늘도 여태것처럼 그냥 잠 들어버려서 못 갈지도 모른다고 생각했다. 하지만 그러기엔 민식이의 눈에는 저기 뜬 달이 너무나 떨렸다.

민식이는 지금 미로 속에 있다. 미로는 직사각형 모양이고, 여행길을 떠나기 위해 미로를 탈출하려고 한다. 미로는 다음과 같이 구성되어져있다.

빈 칸: 언제나 이동할 수 있다. ('.')
벽: 절대 이동할 수 없다. ('#')
열쇠: 언제나 이동할 수 있다. 이 곳에 처음 들어가면 열쇠를 집는다. ('a', 'b', 'c', 'd', 'e', 'f')
문: 대응하는 열쇠가 있을 때만 이동할 수 있다. ('A', 'B', 'C', 'D', 'E', 'F')
민식이의 현재 위치: 빈 곳이고, 민식이가 현재 서 있는 곳이다. ('0')
출구: 달이 차오르기 때문에, 민식이가 가야하는 곳이다. 이 곳에 오면 미로를 탈출한다. ('1')
달이 차오르는 기회를 놓치지 않기 위해서, 미로를 탈출하려고 한다. 한 번의 움직임은 현재 위치에서 수평이나 수직으로 한 칸 이동하는 것이다.

민식이가 미로를 탈출하는데 걸리는 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 미로의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 50) 둘째 줄부터 N개의 줄에 미로의 모양이 주어진다. 같은 타입의 열쇠가 여러 개 있을 수 있고, 문도 마찬가지이다. 그리고, 문에 대응하는 열쇠가 없을 수도 있다. '0'은 한 개, '1'은 적어도 한 개 있다. 열쇠는 여러 번 사용할 수 있다.

출력
첫째 줄에 민식이가 미로를 탈출하는데 드는 이동 횟수의 최솟값을 출력한다. 만약 민식이가 미로를 탈출 할 수 없으면, -1을 출력한다.

예제 입력 1
1 7
f0.F..1
예제 출력 1
7
예제 입력 2
5 5
....1
#1###
.1.#0
....A
.1.#.
예제 출력 2
-1
예제 입력 3
7 8
a#c#eF.1
.#.#.#..
.#B#D###
0....F.1
C#E#A###
.#.#.#..
d#f#bF.1
예제 출력 3
55
예제 입력 4
3 4
1..0
###.
1...
예제 출력 4
3
예제 입력 5
3 5
..0..
.###.
..1.A
예제 출력 5
6
예제 입력 6
4 5
0....
.#B#A
.#.#.
b#a#1
예제 출력 6
19
예제 입력 7
1 11
c.0.C.C.C.1
예제 출력 7
12
예제 입력 8
3 6
###...
#0A.1a
###...
예제 출력 8
-1
출처
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: jh05013, wkd48632
잘못된 조건을 찾은 사람: kesakiyo, ntopia
데이터를 추가한 사람: snengggggggg
'''
from collections import deque
from sys import stdin

readline = stdin.readline

OFFSET = [(0, 1), (0, -1), (1, 0), (-1, 0)]

MINSIK = '0'
WAYOUT = '1'
EMPTY = '.'
WALL = '#'

KEYS = ('a', 'b', 'c', 'd', 'e', 'f')
KEY_MAP = {'a': 2 ** 0, 'b': 2 ** 1, 'c': 2 ** 2, 'd': 2 ** 3, 'e': 2 ** 4, 'f': 2 ** 5}

DOORS = ('A', 'B', 'C', 'D', 'E', 'F')


def find_minsick(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == MINSIK:
                return i, j
    raise ValueError


def solution(maze):
    width, height = len(maze[0]), len(maze)
    cur = (i, j) = find_minsick(maze)

    visited = [[set() for _ in range(width)] for _ in range(height)]

    queue = deque([(cur, 0, 0)])
    visited[i][j].add(0)

    while queue:
        (i, j), step, keys = queue.popleft()

        if maze[i][j] == WAYOUT:
            return step

        for wi, wj in OFFSET:
            nxt = (ni, nj) = i + wi, j + wj

            if ni < 0 or ni >= height or nj < 0 or nj >= width:
                continue

            if keys in visited[ni][nj]:
                continue

            item = maze[ni][nj]
            new_keys = keys

            if item == WALL:
                continue
            elif item in KEYS:
                new_keys |= KEY_MAP[item]
            elif item in DOORS:
                if not KEY_MAP[item.lower()] & keys:
                    continue

            queue.append((nxt, step + 1, new_keys))
            visited[ni][nj].add(new_keys)

    return -1


if __name__ == '__main__':
    N, M = map(int, readline().split())
    maze = [list(readline().rstrip()) for _ in range(N)]
    print(solution(maze))
