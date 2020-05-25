from sys import stdin,setrecursionlimit
offset = ((1,0),(-1,0),(0,1),(0,-1))
setrecursionlimit(10000)

def dfs(x,y,visited):
    for wx, wy in offset:
        nx, ny = x+wx, y+wy
        if not(0 <= nx < N) or not(0 <= ny < N) or not visited[nx][ny] or land[nx][ny] <= n:
             continue
        visited[nx][ny] = False
        dfs(nx,ny,visited)

if __name__ == '__main__':
    N = int(stdin.readline())
    land = [list(map(int,stdin.readline().split())) for _ in range(N)]
    res = 1
    temp = 1
    n = 1
    while temp:
        visited = [[True for _ in range(N)] for _ in range(N)]
        temp = 0

        for i in range(N):
            for j in range(N):
                if land[i][j] > n and visited[i][j]:
                    visited[i][j] = False
                    dfs(i,j,visited)
                    temp += 1
        res = max(res, temp)
        n += 1
    print(res)

'''
5

6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

5
2 100 2 100 2
100 2 100 2 100
2 100 2 100 2
100 2 100 2 100
2 100 2 100 2

5
2 2 2 2 2
2 2 2 2 2
2 2 2 2 2
2 2 2 2 2
2 2 2 2 2

1

7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9

6

2
1 2
2 2


2
1 1
1 1

1



'''
