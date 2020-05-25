'''
섬 연결하기
문제 설명
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항

섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.
입출력 예

n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
입출력 예 설명
'''
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
costs.sort(key=lambda x:(x[2]))
costs
# Kruskal
def find(parents,node):
    try:
        if parents[node] == node:
            return node
        else:
            parents[node] = find(parents,parents[node])
            return parents[node]
    except KeyError:
        parents[node] = node
        return node

def union(parents,left,right):
    l = find(parents,left)
    r = find(parents,right)

    if l < r:
        parents[r] = l
    else:
        parents[l] = r

def solution(n, costs):
    answer = 0
    count = 0
    parents = {}

    for s,e,c in sorted(costs,key=lambda x:(x[2])):
        if count == n-1:
            break

        if find(parents,s) != find(parents,e):
            count += 1
            answer += c

            union(parents,s,e)

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]] #4
solution(n, costs)

n = 4
costs = [[0,1,1],[0,2,2],[2,3,1]]#4
solution(n, costs)

n = 5
costs = [[0,1,1],[1,2,3],[2,3,2],[3,4,1]] #7
solution(n, costs)

n = 5
costs = [[0,1,1],[1,2,1],[3,1,1],[4,3,1]]

solution(n,costs)
