'''
트리의 지름

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	58030	23446	17718	40.699%
문제
트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.



이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.



트리의 노드는 1부터 n까지 번호가 매겨져 있다.

입력
파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

예제 입력 1
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
예제 출력 1
45
출처
문제의 오타를 찾은 사람: apjw6112
데이터를 추가한 사람: dlwjsgud12, shg9411, tony9402, yongdol503
'''
from collections import deque
from sys import stdin

readline = stdin.readline


def search(tree, start):
    max_node, max_dist = 0, 0
    visited = [False] * len(tree)
    queue = deque([(start, 0)])

    visited[start] = True

    while queue:
        cur, total_cost = queue.popleft()

        if total_cost > max_dist:
            max_dist = total_cost
            max_node = cur

        for nxt, cost in tree[cur]:
            if visited[nxt]:
                continue

            queue.append((nxt, total_cost + cost))
            visited[nxt] = True

    return max_node, max_dist


if __name__ == '__main__':
    n = int(readline())
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        s, e, c = map(int, readline().split())
        tree[s].append((e, c))
        tree[e].append((s, c))

    node, _ = search(tree, 1)
    _, dist = search(tree, node)

    print(dist)
