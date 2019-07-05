'''
파일 합치기
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	7954	4213	2676	52.154%
문제
소설가인 김대전은 소설을 여러 장(chapter)으로 나누어 쓰는데, 각 장은 각각 다른 파일에 저장하곤 한다.
소설의 모든 장을 쓰고 나서는 각 장이 쓰여진 파일을 합쳐서 최종적으로 소설의 완성본이 들어있는 한 개의 파일을 만든다.
이 과정에서 두 개의 파일을 합쳐서 하나의 임시파일을 만들고,
이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 소설의 여러 장들이 연속이 되도록 파일을 합쳐나가고,
최종적으로는 하나의 파일로 합친다.
두 개의 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합이라고 가정할 때,
최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합을 계산하시오.

예를 들어, C1, C2, C3, C4가 연속적인 네 개의 장을 수록하고 있는 파일이고,
파일 크기가 각각 40, 30, 30, 50 이라고 하자.
이 파일들을 합치는 과정에서, 먼저 C2와 C3를 합쳐서 임시파일 X1을 만든다.
이때 비용 60이 필요하다.
그 다음으로 C1과 X1을 합쳐 임시파일 X2를 만들면 비용 100이 필요하다.
최종적으로 X2와 C4를 합쳐 최종파일을 만들면 비용 150이 필요하다.
따라서, 최종의 한 파일을 만드는데 필요한 비용의 합은 60+100+150=310 이다.
다른 방법으로 파일을 합치면 비용을 줄일 수 있다.
먼저 C1과 C2를 합쳐 임시파일 Y1을 만들고,
C3와 C4를 합쳐 임시파일 Y2를 만들고,
최종적으로 Y1과 Y2를 합쳐 최종파일을 만들 수 있다.
이때 필요한 총 비용은 70+80+150=300 이다.

소설의 각 장들이 수록되어 있는 파일의 크기가 주어졌을 때,
이 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하는 프로그램을 작성하시오.

입력
프로그램은 표준 입력에서 입력 데이터를 받는다.
프로그램의 입력은 T개의 테스트 데이터로 이루어져 있는데,
T는 입력의 맨 첫 줄에 주어진다.
각 테스트 데이터는 두 개의 행으로 주어지는데,
첫 행에는 소설을 구성하는 장의 수를 나타내는 양의 정수 K (3 ≤ K ≤ 500)가 주어진다.
두 번째 행에는 1장부터 K장까지 수록한 파일의 크기를 나타내는 양의 정수 K개가 주어진다.
파일의 크기는 10,000을 초과하지 않는다.

출력
프로그램은 표준 출력에 출력한다.
각 테스트 데이터마다 정확히 한 행에 출력하는데,
모든 장을 합치는데 필요한 최소비용을 출력한다.

예제 입력 1
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
예제 출력 1
300
864
출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition
> Daejeon Nationalwide Internet Competition 2015 F번
'''
# from sys import stdin,setrecursionlimit
# input = stdin.readline
# setrecursionlimit(2500)
#
# def dp(i,j):
#     if i==j:
#         return 0
#     try:
#         return sums[i,j]
#     except KeyError:
#         sums[i,j] = sizes[j+1]-sizes[i] + min(dp(i,k)+dp(k+1,j) for k in range(i,j))
#         return sums[i,j]
#
# T = int(input())
#
# for _ in range(T):
#     sums = {}
#     K = int(input())
#     sizes = [0]
#     for f in map(int,input().split()):
#         sizes.append(sizes[-1]+f)
#     print(dp(0,K-1))
################################################################################
# from sys import stdin
# input = stdin.readline
#
# for _ in range(int(input())):
#     n = int(input())
#     sums = [0]
#     opt = [[0]*(n+1) for _ in range(n)]
#     dp = [[0]*(n+1) for _ in range(n+1)]
#
#     for i,f in enumerate(map(int,input().split()),1):
#         sums.append(sums[-1]+f)
#         opt[i-1][i] = i
#
#     for d in range(2,n+1):
#         for i in range(n-d+1):
#             print(i,i+d)
#             dp[i][i+d], opt[i][i+d] = min(((dp[i][k]+dp[k][i+d],k) for k in range(opt[i][d+i-1],opt[i+1][i+d]+1)),key=lambda x:x[0])
#             dp[i][i+d] += sums[i+d]-sums[i]
#     print(dp[0][-1])
#     for s in dp:print(s)
#     print()
#     for o in opt:print(o)
# ################################################################################
# from sys import stdin
# input = stdin.readline
#
# for _ in range(int(input())):
#     n = int(input())
#     opt = {(i-1,i):i for i in range(1,n+1)}
#     files = list(map(int,input().split()))
#     sums = [0]
#     for s in files:
#         sums.append(sums[-1]+s)
#
#     dp = {}
#     for i in range(n+2):
#         dp[i,i] = 0
#         dp[i,i+1] = 0
#         try:
#             dp[i,i+2] = files[i]+files[i+1]
#         except:
#             continue
#
#     for d in range(2,n+1):
#         for i in range(n-d+1):
#             dp[i,i+d] = float('inf')
#             dp[i,i+d], opt[i,i+d] = min(((dp[i,k]+dp[k,i+d],k) for k in range(opt[i,d+i-1],opt[i+1,i+d]+1)))
#             dp[i,i+d] += sums[i+d]-sums[i]
#
#     print(dp[0,n])
################################################################################
# from sys import stdin
# input = stdin.readline
#
# def dp(n,sums):
#     mem = []
#     knuth = []
#     for i in range(n+2):
#         dp[i,i] = 0
#         dp[i,i+1] = 0
#         try:
#             dp[i,i+2] = files[i]+files[i+1]
#         except:
#             continue
#
#     for d in range(2,n+1):
#         for i in range(n-d+1):
#             dp[i,i+d] = float('inf')
#             dp[i,i+d], opt[i,i+d] = min(((dp[i,k]+dp[k,i+d],k) for k in range(opt[i,d+i-1],opt[i+1,i+d]+1)))
#             dp[i,i+d] += sums[i+d]-sums[i]
#     return
#
# for _ in range(int(input())):
#     n = int(input())
#     sums = [0]
#
#     for s in map(int,input().split()):
#         sums.append(sums[-1]+s)
#
#     print(dp(n,sums))


import sys
input = sys.stdin.readline

def dp(sums, n):
    dp = [[], [0]*n, [sums[i+2] - sums[i] for i in range(n-1)]]
    knuth = [1]*(n-1)

    for d in range(3, n+1):
        dp_temp, knuth_temp = [], []
        for i in range(n-d+1):
            min_sum, opt_k = min(((dp[k][i]+dp[d-k][i+k],k) for k in range(knuth[i], knuth[i+1]+2)),key=lambda x:x[0])
            dp_temp.append(min_sum + sums[i+d]-sums[i])
            knuth_temp.append(opt_k)
        dp.append(dp_temp)
        knuth = knuth_temp

    return dp[n][0]

for _ in range(int(input())):
    n = int(input())
    sums = [0]

    for chapter in map(int, input().split()):
        sums.append(sums[-1] + chapter)
    print(dp(sums, n))
