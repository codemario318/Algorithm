'''
트리의 지름 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	17425	6300	4582	35.082%
문제
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

입력
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

예제 입력 1 
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
예제 출력 1 
11
출처
문제의 오타를 찾은 사람: ababc1005, cfghj101, WeissBlume
문제를 만든 사람: author5
데이터를 추가한 사람: djm03178
'''
# 트리의 지름 특성 증명
# https://www.quora.com/How-does-following-algorithm-for-finding-longest-path-in-tree-work
from sys import stdin
from collections import deque

readline = stdin.readline


def bfs(cur):
    visited = [False for _ in range(V+1)]
    q = deque([(cur, 0)])
    max_node, max_dist = 0, 0
    
    visited[cur] = True

    while q:
        cur_node, cur_dist = q.popleft()

        if cur_dist > max_dist:
           max_node, max_dist = cur_node, cur_dist

        for nxt_node, cost in graph[cur_node]:
            if not visited[nxt_node]:
                visited[nxt_node] = True
                q.append((nxt_node, cur_dist + cost))

    return max_node, max_dist

V = int(readline())
graph = {}
visited = []

for _ in range(V):
    node, *edges = map(int, readline().split())
    graph[node] = [(edges[i], edges[i + 1]) for i in range(0, len(edges) - 1, 2)]

nxt, _ = bfs(1)
_, res = bfs(nxt)

print(res)