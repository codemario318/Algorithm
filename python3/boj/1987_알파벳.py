'''
알파벳 실패출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	50184	15811	9651	29.098%
문제
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력 1 
2 4
CAAB
ADCB
예제 출력 1 
3
출처
Olympiad > Croatian Highschool Competitions in Informatics > 2002 > Regional Competition - Juniors 3번

데이터를 추가한 사람: august14, doju, jh05013
링크
PKU Judge Online
'''
from sys import stdin
from collections import deque

readline = stdin.readline
OFFSET = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def get_pos(alpha):
    return ord(alpha) - ord('A')


def search():
    used = [False for _ in range(26)]
    q = deque([(0, 0, 1)])

    used[get_pos(board[0][0])] = True
    res = 1

    while q:
        i, j, t, used = q.popleft()

        if t > res:
            res = t

        for wi, wj in OFFSET:
            ni, nj = i+wi, j+wj
            if 0 <= ni < R and 0 <= nj < C and not used[get_pos(board[ni][nj])]:
                used[get_pos(board[ni][nj])] = True
                q.append((ni, nj, t+1, used | {board[ni][nj]}))

    return res


R, C = map(int, readline().split())
board = [readline().rstrip() for _ in range(R)]

print(search(0, 0, 1))


# DFS
# def search(i, j, res):
#     global answer

#     answer = max(answer, res)

#     for wi, wj in OFFSET:
#         ni, nj = i+wi, j+wj

#         if 0 <= ni < R and 0 <= nj < C and not used[get_pos(board[ni][nj])]:
#             used[get_pos(board[ni][nj])] = True
#             search(ni, nj, res+1)
#             used[get_pos(board[ni][nj])] = False

#     return res

# def search():
#     q = deque([(0, 0, 1, set([board[0][0]]))])
#     # D = [[0 for _ in range(C)] for _ in range(R)]

#     # D[0][0] = 1
#     res = 1

#     while q:
#         i, j, t, used = q.popleft()

#         if t > res:
#             res = t

#         for wi, wj in OFFSET:
#             ni, nj = i+wi, j+wj

#             # if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in used and D[ni][nj] <= t:
#             if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in used:
#                 # D[ni][nj] = t+1
#                 q.append((ni, nj, t+1, used | {board[ni][nj]}))

#     return res
