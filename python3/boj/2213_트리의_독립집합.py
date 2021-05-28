'''
트리의 독립집합 스페셜 저지분류
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	2988	1438	1093	49.479%
문제
그래프 G(V, E)에서 정점의 부분 집합 S에 속한 모든 정점쌍이 서로 인접하지 않으면 (정점쌍을 잇는 에지가 없으면) S를 독립 집합(independent set)이라고 한다. 독립 집합의 크기는 정점에 가중치가 주어져 있지 않을 경우는 독립 집합에 속한 정점의 수를 말하고, 정점에 가중치가 주어져 있으면 독립 집합에 속한 정점의 가중치의 합으로 정의한다. 독립 집합이 공집합일 때 그 크기는 0이라고 하자. 크기가 최대인 독립 집합을 최대 독립 집합이라고 한다.

문제는 일반적인 그래프가 아니라 트리(연결되어 있고 사이클이 없는 그래프)와 각 정점의 가중치가 양의 정수로 주어져 있을 때, 최대 독립 집합을 구하는 것이다.

입력
첫째 줄에 트리의 정점의 수 n이 주어진다. n은 10,000이하인 양의 정수이다. 1부터 n사이의 정수가 트리의 정점이라고 가정한다. 둘째 줄에는 n개의 정수 w1, w2, ..., wn이 주어지는데, wi는 정점 i의 가중치이다(1 ≤ i ≤ n). 셋째 줄부터 마지막 줄까지는 에지 리스트가 주어지는데, 한 줄에 하나의 에지를 나타낸다. 에지는 정점의 쌍으로 주어진다. 입력되는 정수들 사이에는 콤마가 없고 대신 빈칸이 하나 혹은 그 이상 있다. 가중치들의 값은 10,000을 넘지 않는 자연수이다.

출력
첫째 줄에 최대 독립집합의 크기를 출력한다. 둘째 줄에는 최대 독립집합에 속하는 정점을 오름차순으로 출력한다. 최대 독립 집합이 하나 이상일 경우에는 하나만 출력하면 된다.

예제 입력 1 
7
10 30 40 10 20 20 70
1 2
2 3
4 3
4 5
6 2
6 7
예제 출력 1 
140
1 3 5 7
출처
잘못된 데이터를 찾은 사람: yigun1029
'''
from sys import stdin

readline = stdin.readline


def search(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        search(nxt, cur)
        mem[cur][0] += max(mem[nxt])
        mem[cur][1] += mem[nxt][0]


def trace(cur, prev, used):
    if used:
        visited.append(cur)
        for nxt in graph[cur]:
            if prev == nxt:
                continue
            trace(nxt, cur, False)
    else:
        for nxt in graph[cur]:
            if prev == nxt:
                continue

            if mem[nxt][0] > mem[nxt][1]:
                trace(nxt, cur, False)
            else:
                trace(nxt, cur, True)


N = int(readline())
weights = [0] + list(map(int, readline().split()))
graph = [[] for _ in range(N + 1)]
mem = [[0, weights[i]] for i in range(N + 1)]
visited = []

for _ in range(N - 1):
    s, e = map(int, readline().split())
    graph[s].append(e)
    graph[e].append(s)

search(1, 1)

if mem[1][0] > mem[1][1]:
    trace(1, 1, 0)
    print(mem[1][0])
else:
    trace(1, 1, 1)
    print(mem[1][1])

visited.sort()
print(*visited)