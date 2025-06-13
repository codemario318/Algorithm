'''
LCA 2

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1.5 초 (추가 시간 없음) (하단 참고)	256 MB	40732	15093	7821	33.117%
문제
N(2 ≤ N ≤ 100,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.

두 노드의 쌍 M(1 ≤ M ≤ 100,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

입력
첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다. 그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

출력
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.

예제 입력 1
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15
예제 출력 1
2
4
2
1
3
1
출처
문제를 만든 사람: baekjoon
시간 제한을 수정한 사람: jh05013
데이터를 추가한 사람: jyon, spectaclehong
알고리즘 분류
보기

시간 제한
Java 8: 2.5 초
Java 8 (OpenJDK): 2.5 초
Java 11: 2.5 초
Kotlin (JVM): 2.5 초
'''
import math
from sys import stdin, setrecursionlimit

readline = stdin.readline
setrecursionlimit(10 ** 6)


def get_parents_depths(N, tree):
    depths = [0 for _ in range(N + 1)]
    LOG = math.ceil(math.log2(N))
    parents = [[0 for _ in range(LOG)] for _ in range(N + 1)]

    def dfs(node, parent, depth):
        depths[node] = depth
        parents[node][0] = parent

        for nxt in tree[node]:
            if nxt != parent:
                dfs(nxt, node, depth + 1)

    dfs(1, 0, 0)

    for j in range(1, LOG):
        for i in range(1, N + 1):
            if parents[i][j - 1] != 0:
                parents[i][j] = parents[parents[i][j - 1]][j - 1]

    return depths, parents


def lca(depths, parents, a, b):
    if depths[a] < depths[b]:
        a, b = b, a

    diff = depths[a] - depths[b]

    for i in range(len(parents[a])):
        if (diff >> i) & 1:
            a = parents[a][i]

    if a == b:
        return a

    for i in range(len(parents[b]) - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]

    return parents[a][0]


if __name__ == '__main__':
    N = int(readline())
    tree = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        a, b = map(int, readline().split())
        tree[a].append(b)
        tree[b].append(a)

    depths, parents = get_parents_depths(N, tree)

    M = int(readline())

    for _ in range(M):
        a, b = map(int, readline().split())
        print(lca(depths, parents, a, b))
