'''
가장 긴 증가하는 부분 수열
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	34045	12675	8655	37.012%
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에
가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1
6
10 20 10 30 20 50
예제 출력 1
4
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: harinboy
비슷한 문제
11054번. 가장 긴 바이토닉 부분 수열
11055번. 가장 큰 증가 부분 수열
11722번. 가장 긴 감소하는 부분 수열
12015번. 가장 긴 증가하는 부분 수열 2
12738번. 가장 긴 증가하는 부분 수열 3
14002번. 가장 긴 증가하는 부분 수열 4
14003번. 가장 긴 증가하는 부분 수열 5
'''
'''
7
1 2 4 3 6 4 5

6
5 3 4 1 2 3

7
6 1 4 5 2 3 4

8
6 1 4 5 2 3 4 1

'''
# bisect_right([1,2,4],2)
# from sys import stdin
# input = stdin.readline
#
# def dp(n):
#     if cache[n] != -1:
#         return cache[n]
#     else:
#         cache[n] = 1
#         temp = []
#         for a in range(n-1,-1,-1):
#             if A[n] > A[a]:
#                 temp.append((a,dp(a)))
#         if len(temp) == 0:
#             cache[n] = 1
#         else:
#             cache[n] = dp(max(temp,key=lambda x: (x[1],-x[0]))[0])+1
#         return cache[n]
#
# N = int(input())
# A = list(map(int,input().split()))
# cache = [1]+[-1 for _ in range(N-1)]
#
# for n in range(N):
#     dp(n)
# # print(dp(N-1))
# print(max(cache))
# 4
# 4 2 1 3
# 8
# 2 8 6 1 5 4 3 7
from sys import stdin

def lis(n,nums):
    mem = [1 for _ in range(n)]

    for i in range(n):
        temp = 1
        for j in range(i,-1,-1):
            if nums[i] > nums[j]:
                temp = max(temp, mem[j]+1)
        mem[i] = temp
    return mem

if __name__ == '__main__':
    N = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    print(max(lis(N,nums)))
