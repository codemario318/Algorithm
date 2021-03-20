'''
최소비용 구하기 2 스페셜 저지분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	7003	3120	2006	43.196%
문제
n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 항상 시작점에서 도착점으로의 경로가 존재한다.

입력
첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.

출력
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.

셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.

예제 입력 1 
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
예제 출력 1 
4
3
1 3 5

5
9
1 2 2
1 3 3
1 3 2
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5


5
8
1 2 0
1 3 0
1 4 0
1 5 0
2 4 0
3 4 0
3 5 0
4 5 0
1 5


출처
문제를 만든 사람: baekjoon
잘못된 데이터를 찾은 사람: bghgu
문제의 오타를 찾은 사람: operaghost
데이터를 추가한 사람: sait2000
빠진 조건을 찾은 사람: upple1

'''

from sys import stdin
from heapq import heappop, heappush
from collections import deque, defaultdict

readline = stdin.readline


def search(graph, s, e, n):
    D = [float('inf') for _ in range(n+1)]
    hq = [(0, s)]

    D[s] = 0
    path = [0 for _ in range(n+1)]

    while hq:
        cost, cur = heappop(hq)

        if cur == e:
            return cost, get_path(path, s, e)

        for nxt, nc in graph[cur].items():
            total = cost + nc

            if D[nxt] > total:
                D[nxt] = total
                path[nxt] = cur

                heappush(hq, (total, nxt))


def get_path(path, s, e):
    res = deque([e])
    idx = e

    while path[idx] != s:
        prev = path[idx]
        res.appendleft(prev)
        idx = prev

    res.appendleft(s)

    return res


if __name__ == '__main__':
    N = int(readline())
    M = int(readline())

    graph = defaultdict(dict)

    for _ in range(M):
        s, e, c = map(int, readline().split())
        
        if e not in graph[s]:
            graph[s][e] = c
        else:
            graph[s][e] = min(graph[s][e], c)

    s, e = map(int, readline().split())

    cost, path = search(graph, s, e, N)

    print(cost)
    print(len(path))
    print(' '.join(map(str, path)))
