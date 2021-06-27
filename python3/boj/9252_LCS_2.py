'''
LCS 2 스페셜 저지
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	16811	6784	5071	41.041%
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.

예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4
ACAK

AAAA
AAA

3
AAA
'''
from sys import stdin

readline = stdin.readline

s1 = readline().rstrip()
s2 = readline().rstrip()

mem_length = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
mem_string = [['' for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            mem_length[i][j] = mem_length[i - 1][j - 1] + 1
            mem_string[i][j] = mem_string[i - 1][j - 1] + s1[i - 1]
        else:
            mi, mj = max((i, j - 1), (i - 1, j),
                         key=lambda x: mem_length[x[0]][x[1]])
            mem_length[i][j] = mem_length[mi][mj]
            mem_string[i][j] = mem_string[mi][mj]

print(mem_length[-1][-1])

if mem_length[-1][-1] > 0:
    print(mem_string[-1][-1])
