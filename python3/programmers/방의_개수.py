def solution(arrows):
    global graph, paths
    graph = {}
    paths = set()

    answer = 0
    offset = {
        0:( 1, 0 ), 1:( 1, 1 ), 2:( 0, 1 ), 3: ( -1, 1 ),
        4: ( -1, 0 ), 5:( -1, -1 ), 6:( 0, -1 ), 7:( 1, -1 )
    }
    cur_pos = ( 0, 0 )

    for arrow in arrows:
        if cur_pos not in graph:
            graph[cur_pos] = set()

        wx, wy = offset[arrow]
        next_pos = ( cur_pos[0] + wx, cur_pos[1] + wy )

        if next_pos not in graph:
            graph[next_pos] = set()

        graph[cur_pos].add(next_pos)
        graph[next_pos].add(cur_pos)
        cur_pos = next_pos

    print(graph)
    # answer = dfs(graph, (0,0))

    # for k,v in graph.items():
    #     print("Node: {}, nexts: {}".format(k,v))

    # return answer

def dfs(graph, cur_node, visited=set()):
    if cur_node == (0, 0) and len(visited):
        print('yap',visited)
        return 1
    elif cur_node in visited:
        print('no',visited+[cur_node])
        return 0
    else:
        count = 0

        for next_node in graph[cur_node]:
            count += dfs(graph, next_node, visited+[cur_node])

        return count

solution(	[6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])
