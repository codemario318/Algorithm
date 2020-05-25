'''
DFS와 BFS
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	65624	19736	11605	29.426%
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),
간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를,
그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1
1 2 4 3
1 2 3 4
예제 입력 2
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2
3 1 2 5 4
3 1 4 2 5
예제 입력 3
1000 1 1000
999 1000
예제 출력 3
1000 999
1000 999
'''
def dfs(graph,start_node,node_num):
    s = start_node - 1
    visited = [s]
    e = 0
    while len(visited) < node_num:
        if s > node_num-1:
            break
        if e > node_num-1:
            s += 1
            e = 0
            continue
        if graph[s][e] == 1 and e not in visited:
            visited.append(e)
            s = e
            e = 0
        else:
            e += 1
    return visited

def bfs(graph,start_node,node_num,edge_num):
    s = start_node - 1
    visited = [s]
    d = 0
    e = 0
    while len(visited) < node_num and len(visited) < edge_num + 1:
        if s > node_num -1:
            break
        if e > node_num -1:
            d += 1
            s = visited[d]
            e = 0
        if graph[s][e] == 1 and e not in visited:
            visited.append(e)
        e += 1
    return visited

node_num, edge_num, start_node = map(int,input().split())

graph = [[0] * node_num for _ in range(node_num)]

for n in range(edge_num):
    i,j = list(map(int,input().split()))
    graph[i-1][j-1] = 1
    graph[j-1][i-1] = 1

trans = lambda x: str(x+1)

print(' '.join(map(trans,dfs(graph,start_node,node_num))))
print(' '.join(map(trans,bfs(graph,start_node,node_num,edge_num))))
