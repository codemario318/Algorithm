from sys import stdin

def find(k,r):
    for e in graph[k]:
        try:
            if v[e] == e:
                v[e] = r
        except KeyError:
            graph[r].append(e)
    return r

if __name__ == '__main__':
    global res
    N,M = map(int,stdin.readline().split())
    graph = {}

    for _ in range(M):
        k,v = stdin.readline().split()
        try:
            graph[k].append(v)
        except KeyError:
            graph[k] = [v]

    print(graph)
    res = set()
    v = {k:k for k in graph}
    print(v)
    for k in graph:
        if v[k] == k:
            res.add(find(k,k))
    print(res)
    print(v)
