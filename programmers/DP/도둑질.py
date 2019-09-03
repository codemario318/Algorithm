'''
문제 설명
도둑이 어느 마을을 털 계획을 하고 있습니다.
이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.

image.png

각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때,
도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

제한사항
이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.
입출력 예
money	return
[1, 2, 3, 1]	4
'''
money = [1, 2, 3, 1]
###############################################################################
# 시간초과
from sys import setrecursionlimit
setrecursionlimit(1000000)

# def dp(i,money,cache):
#     if cache[i] != -1:
#         return cache[i]
#     else:
#         cache[i] = max(dp(i-2,money,cache),money[i]+dp(i-3,money,cache))
#         return cache[i]
#
# def solution(money):
#     N = len(money)
#     if N == 3:
#         return max(money)
#
#     cache = [
#         [money[0], max(money[:2])] + [-1 for _ in range(N-2)],
#         [0, money[1]] + [-1 for _ in range(N-2)]
#     ]
#     return max(dp(N-2,money[:-1],cache[0]),dp(N-1,[0]+money[1:],cache[1]))
###############################################################################
# 시간초과
from sys import setrecursionlimit
setrecursionlimit(1000000)

def dp(i,money,cache):
    if cache[i] != -1:
        return cache[i]
    else:
        cache[i] = max(dp(i-1,money,cache),money[i]+dp(i-2,money,cache))
        return cache[i]

def solution(money):
    N = len(money)
    if N == 3:
        return max(money)

    cache = [
        [money[0], money[1], money[2] + money[0],max(money[0],money[1])+money[3]]+ [-1 for _ in range(N-3)],
        [money[1], money[2], money[1] + money[3]] + [-1 for _ in range(N-3)]
    ]
    return max(dp(N-2,money[:-1],cache[0]),dp(N-1,[0]+money[1:],cache[1]))
solution(money)
####################################################################################
def solution(money):
    if len(money) == 3:
        return max(money)

    cache = [
        [money[0], money[1], money[2] + money[0],max(money[0],money[1])+money[3]],
        [money[1], money[2], money[1] + money[3]]
    ]

    for m in money[4:]:
        cache[0].append(max(cache[0][-2],cache[0][-3]) + m)
        cache[1].append(max(cache[1][-2],cache[1][-3]) + m)

    return max(*cache[0][-3:-1], cache[1][-1])
########################################################################################
def solution(money):
    N = len(money)

    if N <= 3:
        return max(money)

    cache = [
        [money[0], max(money[:2])] + [0 for _ in range(N-2)],
        [0, money[1]] + [0 for _ in range(N-2)]
    ]

    for i in range(2,N):
        cache[0][i] = max(cache[0][i-1],cache[0][i-2]+money[i])
        cache[1][i] = max(cache[1][i-1],cache[1][i-2]+money[i])

    return max(cache[0][-2], cache[1][-1])
########################################################################################
