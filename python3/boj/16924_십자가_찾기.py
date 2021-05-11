'''
십자가 찾기 스페셜 저지분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	1174	454	333	37.755%
문제
십자가는 가운데에 '*'가 있고, 상하좌우 방향으로 모두 같은 길이의 '*'가 있는 모양이다. 십자가의 크기는 가운데를 중심으로 상하좌우 방향으로 있는 '*'의 개수이다. 십자가의 크기는 1보다 크거나 같아야 한다.

아래 그림은 크기가 1, 2, 3인 십자가이고, 빈 칸은 '.'이다.

              ...*...
      ..*..   ...*...
.*.   ..*..   ...*...
***   *****   *******
.*.   ..*..   ...*...
      ..*..   ...*...
              ...*...
크기가 N×M이고, '.'과 '*'로 이루어진 격자판이 주어진다. 이때, 십자가만을 이용해서 격자판과 같은 모양을 만들 수 있는지 구해보자. 십자가는 서로 겹쳐도 된다. 사용할 수 있는 십자가의 개수는 N×M이하이어야 한다. 격자판의 행은 위에서부터 1번, 열은 왼쪽에서부터 1번으로 번호가 매겨져 있다.

입력
첫째 줄에 격자판의 크기 N, M (3 ≤ N, M ≤ 100)이 주어진다. 둘째 줄부터 N개의 줄에 격자판의 상태가 주어진다.

출력
십자가만 이용해서 입력으로 주어진 격자판을 만들 수 없으면 -1을 출력한다.

만들 수 있는 경우에는 필요한 십자가의 수 k(0 ≤ k ≤ N×M)를 출력한다. 다음 k개의 줄에는 그려야 하는 십자가의 정보 x, y, s를 한 줄에 하나씩 출력한다. x는 십자가 중심의 행의 번호, y는 열의 번호, s는 십자가의 크기이다.

가능한 답이 여러가지인 경우에는 아무거나 출력한다.

예제 입력 1 
6 8
....*...
...**...
..*****.
...**...
....*...
........
예제 출력 1 
3
3 4 1
3 5 2
3 5 1
예제 입력 2 
5 5
.*...
****.
.****
..**.
.....
예제 출력 2 
3
2 2 1
3 3 1
3 4 1
예제 입력 3 
5 5
.*...
***..
.*...
.*...
.....
예제 출력 3 
-1
예제 입력 4 
3 3
*.*
.*.
*.*
예제 출력 4 
-1
출처
문제를 번역한 사람: baekjoon
'''
from sys import stdin
readline = stdin.readline
OFFSET = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_cross_size(board, i, j, N):
    size = []
    print(i,j)
    for n in range(1, N+1):
        cross_count = 0
        for wi, wj in OFFSET:
            ni, nj = i+wi*n, j+wj*n
            if 0 <= ni < H and 0 <= nj < W and board[ni][nj] == '*':
                cross_count += 1
                
        if cross_count == 4:
            size.append(n)
        elif cross_count == 0:
            return size
        else: 
            return []

    return size


H, W = map(int, readline().split())
board = [readline().rstrip() for _ in range(H)]

MAX = min(H, W)
res = []

for i in range(H):
    for j in range(W):
        if board[i][j] == '*':
            size = get_cross_size(board, i, j)
            for s in size:
                res.append((i, j, s))

if res:
    for i, j, size in res:
        print(i+1, j+1, size)
else:
    print(-1)
