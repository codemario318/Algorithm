'''
미로만들기

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	16414	8321	6204	56.559%
문제
n×n 바둑판 모양으로 총 n2개의 방이 있다. 일부분은 검은 방이고 나머지는 모두 흰 방이다. 검은 방은 사면이 벽으로 싸여 있어 들어갈 수 없다. 서로 붙어 있는 두 개의 흰 방 사이에는 문이 있어서 지나다닐 수 있다. 윗줄 맨 왼쪽 방은 시작방으로서 항상 흰 방이고, 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방이다.

시작방에서 출발하여 길을 찾아서 끝방으로 가는 것이 목적인데, 아래 그림의 경우에는 시작방에서 끝 방으로 갈 수가 없다. 부득이 검은 방 몇 개를 흰 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.

아래 그림은 n=8인 경우의 한 예이다.



위 그림에서는 두 개의 검은 방(예를 들어 (4,4)의 방과 (7,8)의 방)을 흰 방으로 바꾸면, 시작방에서 끝방으로 갈 수 있지만, 어느 검은 방 하나만을 흰 방으로 바꾸어서는 불가능하다. 검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성하시오.

단, 검은 방을 하나도 흰방으로 바꾸지 않아도 되는 경우는 0이 답이다.

입력
첫 줄에는 한 줄에 들어가는 방의 수 n(1 ≤ n ≤ 50)이 주어지고, 다음 n개의 줄의 각 줄마다 0과 1이 이루어진 길이가 n인 수열이 주어진다. 0은 검은 방, 1은 흰 방을 나타낸다.

출력
첫 줄에 흰 방으로 바꾸어야 할 최소의 검은 방의 수를 출력한다.

예제 입력 1
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111
예제 출력 1
2
출처
Olympiad > 한국정보올림피아드 > KOI 1997 > 고등부 2번

문제의 오타를 찾은 사람: silvercube
데이터를 추가한 사람: wlaud, yukariko
'''

from sys import stdin
from heapq import heappush, heappop

OPEN = '1'
CLOSE = '0'
OFFSET = [(0, 1), (0, -1), (1, 0), (-1, 0)]
readline = stdin.readline


def search(n, board):
    visited = {(0, 0)}
    queue = [(0, 0, 0)]

    while queue:
        cost, i, j = heappop(queue)

        if (i, j) == (n - 1, n - 1):
            return cost

        for wi, wj in OFFSET:
            nxt = ni, nj = i + wi, j + wj

            if not is_in_range(n, ni, nj) or nxt in visited:
                continue

            heappush(queue, (cost + (board[ni][nj] == CLOSE), ni, nj))
            visited.add(nxt)


def is_in_range(n, i, j):
    return 0 <= i < n and 0 <= j < n


if __name__ == '__main__':
    n = int(readline())
    board = [readline().strip() for _ in range(n)]

    print(search(n, board))
