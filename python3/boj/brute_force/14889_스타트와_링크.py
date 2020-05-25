# from sys import stdin
#
# def solution(d,p):
#     if N//2 == d:
#         return calc(team)
#     else:
#         res = float('inf')
#         for i in range(p+1,N):
#             if res == 0: return 0
#             team[i] = True
#             res = min(solution(d+1,i),res)
#             team[i] = False
#         return res
#
# def calc(team):
#     score = 0
#     for i in range(N):
#         cnt = 1
#         for j in range(N):
#             if i == j: continue
#             if team[i] == team[j]:
#                 score += S[i][j] if team[i] else -S[i][j]
#                 cnt += 1
#             if cnt == N//2: break
#     return abs(score)
#
# if __name__ == "__main__":
#     global N,S
#     N = int(stdin.readline())
#     S = [list(map(int,stdin.readline().split())) for _ in range(N)]
#     team = [False for _ in range(N)]
#     team[0] = True
#
#     print(solution(1,0))

from sys import stdin
from itertools import combinations

def solution(N,S):
    comb = list(combinations(range(N),N//2))
    res = float('inf')
    member = set(range(N))
    for item in comb[:len(comb)//2]:
        if res == 0: return 0
        res = min(res,abs(calc(item)-calc(tuple(member-set(item)))))
    return res

def calc(team):
    score = 0
    for i in team:
        for j in team:
            if i == j: continue
            score += S[i][j]
    return score

if __name__ == "__main__":
    N = int(stdin.readline())
    S = [list(map(int,stdin.readline().split())) for _ in range(N)]

    print(solution(N,S))
