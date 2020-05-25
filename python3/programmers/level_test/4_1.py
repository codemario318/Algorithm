maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
import numpy as np

def solution(maps):
    map_arr = np.array(maps)
    explored = {(0,0):1}
    destination = (map_arr.shape[0]-1,map_arr.shape[1]-1)

    search(map_arr,(0,0),1,explored)

    try:
        return explored[destination]
    except KeyError:
        return False

def path_check(map_arr,pos,d):
    m,n = pos

    if d == 0 and n < map_arr.shape[1]-1:
        if map_arr[m,n+1] == 1:
            return (m,n+1)
    if d == 1 and n > 0:
        if map_arr[m,n-1] == 1:
            return (m,n-1)
    if d == 2 and m < map_arr.shape[0]-1:
        if map_arr[m+1,n] == 1:
            return (m+1,n)
    if d == 3 and m > 0:
        if map_arr[m-1,n] == 1:
            return (m-1,n)
    return False

def search(map_arr,start,before_cost,explored):
    cost = before_cost + 1
    paths = []

    for d in range(4):
        path = path_check(map_arr,start,d)
        if path != False:
            paths.append(path)

    for path in paths:
        try:
            if explored[path] > cost:
                explored[path] = cost
            else:
                continue
        except KeyError:
            explored[path] = cost

        search(map_arr,path,cost,explored)
