'''
N-Queen

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
10 초	128 MB	14343	8306	5394	57.530%

문제

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력

첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력

첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1
8
예제 출력 1
92
출처
문제를 만든 사람: baekjoon
알고리즘 분류
보기

메모
'''
def check(x,y,i,j):
    if x == i or y == j or abs(x-i) == abs(y-j):
        return False
    return True

def solution(d,queen,Y):
    if d == N:
        return 1
    else:
        print(d,queen,Y)
        count = 0
        for i in [y for y in range(N) if Y[y] == True]:
            flag = True
            for x,y in queen:
                flag = check(x,y,d+1,i)
                if not flag:
                    break
            if flag:
                temp = Y.copy()
                temp[i] = False
                count += solution(d+1,queen+[(d+1,i)],temp)
        return count

N = int(input())
print(solution(0,[],[True for _ in range(N)]))
# from copy import deepcopy
#
# def check(x,y,i,j):
#     if y == j:
#         return False
#     if abs(x-i) == abs(y-j):
#         return False
#     return True
#
# def solution(board):
#     if len(board) == 0:
#         return 1
#     else:
#         count = 0
#         for i in range(N):
#             if board[0][i]:
#                 temp = deepcopy(board[1:])
#                 for x in range(len(temp)):
#                     for y in range(N):
#                         if temp[x][y]:
#                             temp[x][y] = check(x,y,-1,i)
#                 count += solution(temp)
#         return count
#
# N = int(input())
# print(solution([[True for _ in range(N)] for _ in range(N)]))
