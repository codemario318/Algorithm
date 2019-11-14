'''
웜홀

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	7698	2647	1637	31.021%

문제

때는 2020년, 백준이는 월드나라의 한 국민이다.
월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다.
(단 도로는 방향이 없으며 웜홀은 방향이 있다.)

웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데,
특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다.
웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다.
한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때,
출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다.

여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.

입력

첫 번째 줄에는 테스트케이스의 개수 TC(1 ≤ TC ≤ 5)가 주어진다.
그리고 두 번째 줄부터 TC개의 테스트케이스가 차례로 주어지는데
각 테스트케이스의 첫 번째 줄에는 지점의 수 N(1 ≤ N ≤ 500),
도로의 개수 M(1 ≤ M ≤ 2500), 웜홀의 개수 W(1 ≤ W ≤ 200)이 주어진다.

그리고 두 번째 줄부터 M+1개의 줄까지 도로의 정보가 주어지는데
각 도로의 정보는 S, E, T 세 정수로 주어진다.

S와 E는 연결된 지점의 번호,
T는 이 도로를 통해 이동하는데 걸리는 시간을 의미한다.

그리고 M+2~M+W+1번째 줄까지
웜홀의 정보가 S, E, T 세 정수로 주어지는데
S는 시작 지점, E는 도착 지점, T는 줄어드는 시간을 의미한다.
T는 10,000보다 작거나 같은 자연수 또는 0이다.

두 지점을 연결하는 도로가 한 개보다 많을 수도 있다.
지점의 번호는 1부터 N까지 자연수로 중복 없이 매겨져 있다.

출력

TC개의 줄에 걸쳐서 만약에 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하면 YES,
불가능하면 NO를 출력한다.

예제 입력 1
2
3 3 1
1 2 2
1 3 4
2 3 1
3 1 3
3 2 1
1 2 3
2 3 4
3 1 8

예제 출력 1
NO
YES


1
5 3 2
1 2 1
3 4 1
4 5 1
2 3 3
5 3 5

1
4 2 2
1 2 1
2 1 1
3 4 1
4 3 1

1
5 1 3
1 2 3
3 4 1
4 5 1
5 3 1
출처
Olympiad > USA Computing Olympiad > 2006-2007 Season > USACO December 2006 Contest > Gold 1번

문제의 오타를 찾은 사람: Acka adgdsda jh05013 xbfld
빠진 조건을 찾은 사람: joeyvalentine kipa00 progresivojs wooljs
잘못된 조건을 찾은 사람: vvv3334
'''

from sys import stdin

input = stdin.readline
minput = lambda: map(int,input().split())

def solution(N,edges):
    BF = [float('inf') for _ in range(N+1)]
    BF[1] = 0

    for n in range(N):
        for s,e,t in edges:
            if BF[e] > t+BF[s]:
                BF[e] = t+BF[s]
                if n == N-1:
                    return 'YES'
    return 'NO'

T = int(input())

for _ in range(T):
    N, M, W = minput()
    edges = []

    for _ in range(M):
        s,e,t = minput()
        edges.append((s,e,t))
        edges.append((e,s,t))

    for _ in range(W):
        s,e,t = minput()
        edges.append((s,e,-t))

    print(solution(N,edges))
