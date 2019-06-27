'''
내리막 길
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	22401	5106	3793	26.700%
문제
여행을 떠난 세준이는 지도를 하나 구하였다.
이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.
한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며,
각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.



현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다.
그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다.
위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.





지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여
제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다.
이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다.
M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.

출력
첫째 줄에 이동 가능한 경로의 수 H를 출력한다.
모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.

예제 입력 1
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
예제 출력 1
3
출처
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > 고등부 3번

데이터를 추가한 사람: cgiosy doju
문제의 오타를 찾은 사람: imgosari
잘못된 데이터를 찾은 사람: mygumi tncks0121

'''
# from sys import stdin,setrecursionlimit
# setrecursionlimit(10000**2)
# W = [(-1,0),(0,-1),(1,0),(0,1)]
#
# def search(m,n):
#     result = 0
#     for mw,nw in W:
#         try:
#             rm = m+mw
#             rn = n+nw
#             if rm >= 0 and rn >= 0 and costs[m+mw][n+nw] > costs[m][n]:
#                 result += dp(rm,rn)
#         except IndexError:
#             continue
#     return result
#
# def dp(m,n):
#     try:
#         return counts[(m,n)]
#     except KeyError:
#         counts[(m,n)] = search(m,n)
#     return counts[(m,n)]
#
# m,n = map(int,stdin.readline().split())
# costs = [list(map(int,stdin.readline().split())) for _ in range(m)]
# counts = {(0,0):1}
# print(dp(m-1,n-1))

################################################################################
from sys import stdin,setrecursionlimit
setrecursionlimit(10000**2)

def dp(m,n):
    try:
        return counts[(m,n)]
    except KeyError:
        result = 0

        if m > 0:
            if costs[m][n] > costs[m-1][n]:
                result += dp(m-1,n)
        if m < M-1:
            if costs[m][n] > costs[m+1][n]:
                result += dp(m+1,n)
        if n > 0:
            if costs[m][n] > costs[m][n-1]:
                result += dp(m,n-1)
        if n < N-1:
            if costs[m][n] > costs[m][n+1]:
                result += dp(m,n+1)

        counts[(m,n)] = result
    return counts[(m,n)]

M,N = map(int,stdin.readline().split())
costs = [list(map(int,stdin.readline().split())) for _ in range(M)]
counts = {(M-1,N-1):1}
print(dp(0,0))
