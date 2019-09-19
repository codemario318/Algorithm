'''
특정한 최단 경로
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	15413	4066	2504	23.093%

문제

방향성이 없는 그래프가 주어진다.
세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.

또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데,
그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.
하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
1번 정점에서 N번 정점으로 이동할 때,
주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력

첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)

둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데,
a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000)

다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호가 주어진다.

출력

첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다.
그러한 경로가 없을 때에는 -1을 출력한다.

예제 입력 1
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

4 6
1 2 100
2 3 100
3 4 1
1 3 100
2 4 1
1 4 1
2 3

5 6
1 2 1
1 3 100
1 4 1
2 3 100
2 4 1
3 4 1
2 3

4 3
1 2 1
1 4 1
2 4 1
2 3

예제 출력 1
7
출처
문제의 오타를 찾은 사람: ZZangZZang
알고리즘 분류
보기

메모
메모 작성하기
'''

from sys import stdin
from heapq import heappop, heappush
input = lambda:map(int,stdin.readline().split())

def search(s,f):
    q = [(0,s)]
    D = [float('inf') for _ in range(N)]
    D[s] = 0

    while q:
        w,p = heappop(q)
        for nw,np in graph[p]:
            if D[np] >= nw+w:
                D[np] = w+nw
                heappush(q,(D[np],np))

    return D[f]

N,E = input()
graph = [list() for _ in range(N)]

for _ in range(E):
    a,b,w = input()
    graph[a-1].append((w,b-1))
    graph[b-1].append((w,a-1))

T = list(map(lambda x:x-1,input()))
res = min(search(0,T[0])+search(*T)+search(N-1,T[1]),search(0,T[1])+search(*T)+search(N-1,T[0]))
print(-1 if res == float('inf') else res)
