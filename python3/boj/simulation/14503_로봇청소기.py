'''
로봇 청소기 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	23312	12269	7961	51.658%
문제
로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 각 칸은 (r, c)로 나타낼 수 있고, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.

로봇 청소기는 다음과 같이 작동한다.

현재 위치를 청소한다.
현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

입력
첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)

둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.

로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.

출력
로봇 청소기가 청소하는 칸의 개수를 출력한다.

예제 입력 1 
3 3
1 1 0
1 1 1
1 0 1
1 1 1
예제 출력 1 
1
예제 입력 2 
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
예제 출력 2 
57

3 3
1 1 0
1 1 1
1 1 1
1 1 1


출처
문제의 오타를 찾은 사람: adfsfsf h0ngjun7 jh05013
문제를 만든 사람: baekjoon
데이터를 추가한 사람: exponential_e
어색한 표현을 찾은 사람: jh05013
'''

from sys import stdin
def readline(): return map(int, stdin.readline().split())


def clean(board, x, y):
    if board[x][y] == 0:
        board[x][y] = -1
        return True
    return False


def check(board, x, y):
    return True if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 0 else False


def back_check(board, x, y):
    return True if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != 1 else False


def turn(d):
    d -= 1
    return d if d >= 0 else 3


def robot(board, r, c, d):
    offset = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북, 동, 남, 서
    result = 0

    while True:
        result += clean(board, r, c)
        for _ in range(len(offset)):
            d = turn(d)

            wr, wc = offset[d]
            nr, nc = r+wr, c+wc

            if check(board, nr, nc):
                r, c = nr, nc
                break
        else:
            bnr, bnc = r-wr, c-wc
            if back_check(board, bnr, bnc):
                r, c = bnr, bnc
            else:
                return result


if __name__ == "__main__":
    n, m = readline()
    r, c, d = readline()

    board = [list(readline()) for _ in range(n)]
    print(robot(board, r, c, d))
