'''
치즈 출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	9317	4561	3395	50.259%
문제
아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고, 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다. 판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다. 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다. <그림 1>의 경우, 치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어져서 <그림 2>와 같이 된다.



다시 한 시간 후에는 <그림 2>에서 ‘c’로 표시된 부분이 녹아 없어져서 <그림 3>과 같이 된다.



<그림 3>은 원래 치즈의 두 시간 후 모양을 나타내고 있으며, 남은 조각들은 한 시간이 더 지나면 모두 녹아 없어진다. 그러므로 처음 치즈가 모두 녹아 없어지는 데는 세 시간이 걸린다. <그림 3>과 같이 치즈가 녹는 과정에서 여러 조각으로 나누어 질 수도 있다.

입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때, 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고, 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.

예제 입력 1 
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
예제 출력 1 
3
5

5 5
0 0 0 0 0
0 1 1 0 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0

1
7

4 6
0 0 0 0 0 0
0 0 0 1 1 0
0 1 1 1 1 0
0 0 0 0 0 0

1
6

6 4
0 0 0 0
0 1 1 0
0 0 1 0
0 1 0 0
0 1 0 0
0 0 0 0

1
5

6 6
0 0 0 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
0 0 0 0 0 0

1
3

3 3
0 0 0
0 1 0
0 0 0

1
1

3 3
0 0 0
0 0 0
0 0 0

0
0

5 5 
0 0 0 0 0
0 1 1 0 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0

7 7
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0

3
1

7 7
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 1 1 0 1 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0

2
8

7 7
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 0 1 1 0
0 1 1 0 1 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0

2
7

7 7
0 0 0 0 0 0 0
0 1 1 0 1 1 0
0 1 1 0 1 1 0
0 1 1 0 1 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0

2
2

7 7
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 0 0 0 1 0
0 1 0 1 0 1 0
0 1 0 0 0 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0

9 9
0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0
0 1 0 0 0 0 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0


8 8
0 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0
0 1 0 0 0 1 0 0
0 1 0 1 1 1 0 0
0 1 0 1 1 1 1 0
0 1 1 1 1 0 1 0
0 0 0 0 1 1 1 0
0 0 0 0 0 0 0 0

3
1

출처
Olympiad > 한국정보올림피아드 > KOI 2000 > 초등부 3번

문제의 오타를 찾은 사람: compro0317, shawn050912
데이터를 추가한 사람: jung2381187
'''
from sys import stdin
from collections import deque

OFFSET = ((0, 1), (1, 0), (-1, 0), (0, -1))


def readline():
    return map(int, stdin.readline().split())


def checkAir(cheese, i, j, N, M):
    for wi, wj in OFFSET:
        ni, nj = i+wi, j+wj
        if ni == 0 or ni == N-1 or nj == 0 or nj == M-1:
            return True
        elif (1 <= ni < N-1 and 1 <= nj < M-1 and cheese[ni][nj] == 'a'):
            return True
    return False


def getAir(cheese, N, M):
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 0 and checkAir(cheese, i, j, N, M):
                return i, j


def markAir(cheese, N, M, i, j):
    queue = deque([(i, j)])
    cheese[i][j] = 'a'

    while queue:
        x, y = queue.popleft()

        for wx, wy in OFFSET:
            nx, ny = x+wx, y+wy
            if 0 <= nx < N and 0 <= ny < M and cheese[nx][ny] == 0 and checkAir(cheese, nx, ny, N, M):
                cheese[nx][ny] = 'a'
                queue.append((nx, ny))


def markAirs(cheese, N, M):
    while True:
        cur = getAir(cheese, N, M)
        if cur:
            markAir(cheese, N, M, *cur)
        else:
            break

def markMelt(cheese, N, M):
    count = 0

    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1 and checkAir(cheese, i, j, N, M):
                cheese[i][j] = 'c'

            if cheese[i][j] != 1:
                count += 1
    return count


def meltCheese(cheese, N, M):
    count = 0

    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 'c':
                count += 1
                cheese[i][j] = 'a'
    return count


def prt(cheese):
    print()
    for c in cheese:
        print(' '.join(map(str, c)))
    print()


if __name__ == "__main__":
    N, M = readline()

    cheese = [list(readline()) for _ in range(N)]

    count = 0
    meltCount = 0
    cheeseCount = 0

    while meltCount != M*N:
        markAirs(cheese, N, M)
        meltCount = markMelt(cheese, N, M)
        cheeseCount = meltCheese(cheese, N, M)
        count += 1

    if cheeseCount:
        print(count)
        print(cheeseCount)
    else:
        print(0)
        print(0)
