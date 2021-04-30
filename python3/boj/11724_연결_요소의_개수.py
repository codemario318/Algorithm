'''
연결 요소의 개수 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
3 초	512 MB	42688	20403	13312	44.861%
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
예제 입력 2 
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2 
1
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: djm03178, YunGoon
잘못된 조건을 찾은 사람: songjuh
'''
from sys import stdin

readline = lambda : map(int, stdin.readline().split())

def search(graph, i, visited):
    q = [i]
    visited[i] = True
    
    while q:
        cur = q.pop(0)

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)


N, M = readline()
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = readline()
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(N+1)]
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        search(graph, i, visited)

print(cnt)