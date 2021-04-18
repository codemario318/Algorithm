'''
파이프 옮기기 1 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	13289	6434	4253	48.308%
문제
유현이가 새 집으로 이사했다. 새 집의 크기는 N×N의 격자판으로 나타낼 수 있고, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽이다.

오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 파이프는 아래와 같은 형태이고, 2개의 연속된 칸을 차지하는 크기이다.



파이프는 회전시킬 수 있으며, 아래와 같이 3가지 방향이 가능하다.



파이프는 매우 무겁기 때문에, 유현이는 파이프를 밀어서 이동시키려고 한다. 벽에는 새로운 벽지를 발랐기 때문에, 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.

파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 파이프는 밀면서 회전시킬 수 있다. 회전은 45도만 회전시킬 수 있으며, 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.

파이프가 가로로 놓여진 경우에 가능한 이동 방법은 총 2가지, 세로로 놓여진 경우에는 2가지, 대각선 방향으로 놓여진 경우에는 3가지가 있다.

아래 그림은 파이프가 놓여진 방향에 따라서 이동할 수 있는 방법을 모두 나타낸 것이고, 꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.



가로



세로



대각선

가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.

입력
첫째 줄에 집의 크기 N(3 ≤ N ≤ 16)이 주어진다. 둘째 줄부터 N개의 줄에는 집의 상태가 주어진다. 빈 칸은 0, 벽은 1로 주어진다. (1, 1)과 (1, 2)는 항상 빈 칸이다.

출력
첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력한다. 이동시킬 수 없는 경우에는 0을 출력한다. 방법의 수는 항상 1,000,000보다 작거나 같다.

예제 입력 1 
3
0 0 0
0 0 0
0 0 0
예제 출력 1 
1
예제 입력 2 
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
예제 출력 2 
3
예제 입력 3 
5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
예제 출력 3 
0
예제 입력 4 
6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
예제 출력 4 
13
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: djm03178
'''
from sys import stdin

readline = stdin.readline


def search(house, N):
    mem = [[{'v': 0, 'h': 0, 'c': 0} for _ in range(N+1)] for _ in range(N+1)]
    mem[1][2]['v'] = 1

    for i in range(1, N+1):
        for j in range(1, N+1):
            if house[i][j]:
                continue

            mem[i][j]['v'] += mem[i][j-1]['v'] + mem[i][j-1]['c']
            mem[i][j]['h'] += mem[i-1][j]['h'] + mem[i-1][j]['c']

            if not house[i-1][j] and not house[i][j-1]:
                mem[i][j]['c'] += sum(mem[i-1][j-1].values())

    return sum(mem[-1][-1].values())


if __name__ == '__main__':
    N = int(readline())
    house = [[0] * (N+1)] + [[0] + list(map(int, readline().split()))
                             for _ in range(N)]
    print(search(house, N))



# OFFSET = {
#     'v': [(0, 1, 'v'), (1, 1, 'c')],
#     'h': [(1, 0, 'h'), (1, 1, 'c')],
#     'c': [(0, 1, 'v'), (1, 0, 'h'), (1, 1, 'c')]
# }

# AREA = {
#     'v': [(0, 1)],
#     'h': [(1, 0)],
#     'c': [(0, 1), (1, 0), (1, 1)],
# }

# def search(house, N):
#     count = 0
#     q = deque([(0, 1, 'v')])

#     while q:
#         x, y, p = q.popleft()

#         if x == N-1 and y == N-1:
#             count += 1
#             continue

#         temp = []

#         for wx, wy, np in OFFSET[p]:
#             nx, ny = x+wx, y+wy

#             for ax, ay in AREA[np]:
#                 nax, nay = x+ax, y+ay
#                 if 0 <= nax < N and 0 <= nay < N and not house[nax][nay]:
#                     continue
#                 else:
#                     break
#             else:
#                 q.append((nx, ny, np))
#     return count


# if __name__ == '__main__':
#     N = int(readline())
#     house = [list(map(int, readline().split())) for _ in range(N)]

#     if house[N-1][N-1] == 1:
#         print(0)
#     else:
#         print(search(house, N))
