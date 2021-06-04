'''
트리 출처다국어분류
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	3234	1151	825	33.839%
문제
그래프는 정점과 간선으로 이루어져 있다. 두 정점 사이에 경로가 있다면, 두 정점은 연결되어 있다고 한다. 연결 요소는 모든 정점이 서로 연결되어 있는 정점의 부분집합이다. 그래프는 하나 또는 그 이상의 연결 요소로 이루어져 있다.

트리는 사이클이 없는 연결 요소이다. 트리에는 여러 성질이 있다. 예를 들어, 트리는 정점이 n개, 간선이 n-1개 있다. 또, 임의의 두 정점에 대해서 경로가 유일하다.

그래프가 주어졌을 때, 트리의 개수를 세는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 n ≤ 500과 m ≤ n(n-1)/2을 만족하는 정점의 개수 n과 간선의 개수 m이 주어진다. 다음 m개의 줄에는 간선을 나타내는 두 개의 정수가 주어진다. 같은 간선은 여러 번 주어지지 않는다. 정점은 1번부터 n번까지 번호가 매겨져 있다. 입력의 마지막 줄에는 0이 두 개 주어진다.

출력
입력으로 주어진 그래프에 트리가 없다면 "No trees."를, 한 개라면 "There is one tree."를, T개(T > 1)라면 "A forest of T trees."를 테스트 케이스 번호와 함께 출력한다.

예제 입력 1 
6 3
1 2
2 3
3 4
6 5
1 2
2 3
3 4
4 5
5 6
6 6
1 2
2 3
1 3
4 5
5 6
6 4
0 0

예제 출력 1 
Case 1: A forest of 3 trees.
Case 2: There is one tree.
Case 3: No trees.

9 9
1 2
2 3
3 4
4 5
3 5
6 7
7 8
6 8
8 9
0 0

Case 1: No trees.

4 4
2 3
2 4
3 4
1 2
0 0

Case 1: No trees.

4 4
1 2
2 3
3 1
4 1
0 0

Case 1: No trees.


6 6
1 2
2 3
4 5
5 6
4 6
3 4

Case 1: No trees.


출처
ICPC > Regionals > North America > Rocky Mountain Regional > 2012 Rocky Mountain Regional Contest H번

문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: jh05013
데이터를 추가한 사람: jinhan814
'''
from sys import stdin
from collections import deque

readline = stdin.readline


def bfs(s):
    q = deque([(s, 0)])
    visited[s] = True
    while q:
        cur, prev = q.popleft()

        for nxt in graph[cur]:
            if cur == nxt:
                return False

            if nxt == prev:
                continue

            if not visited[nxt]:
                q.append((nxt, cur))
                visited[nxt] = True
            else:
                return False
    return True


T = 1

while True:
    N, M = map(int, readline().split())

    if not N and not M:
        break

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(N + 1)]
    cnt = 0

    for i in range(1, N + 1):
        if visited[i]:
            continue

        if bfs(i):
            cnt += 1
        else:
            print(f"Case {T}: No trees.")
            break
    else:
        if cnt > 1:
            print(f"Case {T}: A forest of {cnt} trees.")
        else:
            print(f"Case {T}: There is one tree.")

    T += 1
