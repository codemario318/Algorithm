'''
LCS
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	13634	5807	4289	42.074%
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며,
최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

AOLDMKEPPA
OCACKEMPPA

예제 입력 1
ACAYKP
CAPCAK
예제 출력 1
4
출처
문제를 만든 사람: baekjoon
'''
# from sys import setrecursionlimit
# setrecursionlimit(1000**2)
#
# def dp(i,j):
#     if counts[i][j] == None:
#         if i < 1 or j < 1:
#             counts[i][j] = 0
#         else:
#             counts[i][j] = dp(i-1,j-1)+1 if P1[i-1] == P2[j-1] else max(dp(i,j-1),dp(i-1,j))
#     return counts[i][j]
# P1 = input()
# P2 = input()
# counts = [[None]*(len(P2)+1) for _ in range(len(P1)+1)]
# print(dp(len(P1),len(P2)))
################################################################################
# def dp(p1,p2):
#     counts = [[0]*(len(p2)+1) for _ in range(len(p1)+1)]
#     for i in range(0,len(p1)):
#         for j in range(0,len(p2)):
#             counts[i+1][j+1] = counts[i][j]+1 if p1[i] == p2[j] else max(counts[i][j+1],counts[i+1][j])
#     return counts[-1][-1]
#
# P1 = input()
# P2 = input()
#
# print(dp(P1,P2))
################################################################################
from sys import stdin
def dp(p1,p2):
    memo = [0 for _ in range(len(p2)+1)]
    for i in range(len(p1)):
        temp = [0]
        for j in range(len(p2)):
            temp.append(memo[j]+1 if p1[i]==p2[j] else max(temp[j],memo[j+1]))
        memo = temp
    return memo[-1]

P1 = stdin.readline().rstrip()
P2 = stdin.readline().rstrip()

print(dp(P1,P2))
