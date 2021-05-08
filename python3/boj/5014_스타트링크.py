from sys import stdin
from collections import deque

if __name__ == '__main__':
    # F:총 층, S: 현재층 ,G:목적층, U:올라가는층수, D:내려가는층수
    #  (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000)

    F, S, G, U, D = map(int, stdin.readline().split())

    q = deque([(S, 0)])
    visited = [False for _ in range(F+1)]
    visited[S] = True

    while q:
        cur, cost = q.popleft()

        if cur == G:
            print(cost)
            break

        up = cur + U
        down = cur - D

        if 0 < up <= F and not visited[up]:
            q.append((up, cost+1))
            visited[up] = True

        if 0 < down <= F and not visited[down]:
            q.append((down, cost+1))
            visited[down] = True
    else:
        print("use the stairs")
