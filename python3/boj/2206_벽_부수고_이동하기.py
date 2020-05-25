from sys import stdin
from collections import deque
offset = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(path):
    while path:
        d,b,(x,y) = path.popleft()

        if (x,y) == (N-1,M-1):
            return d

        for wx,wy in offset:
            nx = x+wx; ny = y+wy

            if not (0 <= nx < N) or not (0 <= ny < M) or visited[nx][ny][b]:
                continue

            if maps[nx][ny] == '0':
                path.append((d+1,b,(nx,ny)))
                visited[nx][ny][b] = True

            if maps[nx][ny] == '1' and b:
                path.append((d+1,False,(nx,ny)))
                visited[nx][ny][b] = True
    return -1

if __name__ == '__main__':
    N,M = map(int,stdin.readline().split())
    maps = [list(stdin.readline().strip()) for _ in range(N)]
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]
    path = deque([(1,True,(0,0))])
    visited[0][0][0] = True
    print(bfs(path))

'''
4 4
0101
0101
0001
1110

7

6 4
0100
1110
1000
0000
0111
0000

15

4 4
0111
1111
1111
1110

-1

8 4
0000
0110
1110
0000
0111
0000
1110
0000

11
'''

# from sys import stdin
# from heapq import heappop, heappush
# offset = ((0,1),(0,-1),(1,0),(-1,0))
#
# def bfs(path):
#     while path:
#         d,b,(x,y) = heappop(path)
#
#         if (x,y) == (N-1,M-1):
#             return d
#
#         for wx,wy in offset:
#             nx = x+wx; ny = y+wy
#
#             if not (0 <= nx < N) or not (0 <= ny < M) or visited[nx][ny][b]:
#                 continue
#
#             if maps[nx][ny] == '0':
#                 heappush(path,(d+1,b,(nx,ny)))
#                 visited[nx][ny][b] = True
#
#             if maps[nx][ny] == '1' and not b:
#                 heappush(path,(d+1,True,(nx,ny)))
#                 visited[nx][ny][b] = True
#     return -1
#
# if __name__ == '__main__':
#     N,M = map(int,stdin.readline().split())
#     maps = [list(stdin.readline().strip()) for _ in range(N)]
#     visited = [[[False, False] for _ in range(M)] for _ in range(N)]
#     path = [(1,False,(0,0))]
#     visited[0][0][0] = True
#     print(bfs(path))
