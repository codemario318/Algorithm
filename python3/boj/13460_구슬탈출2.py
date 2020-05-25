'''
예제입력 1
5 5
#####
#..B#
#.#.#
#RO.#
#####

예제 출력 1
1
예제 입력 2

7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######

예제 출력 2
5

7 7
#######
#...R.#
#.#####
#.....#
#####.#
#O....#
#######

5 5
#####
#...#
#.#.#
#RO.#
#####

'''
from sys import stdin, setrecursionlimit
# setrecursionlimit(10)
offset = ((0,1),(0,-1),(1,0),(-1,0))

def marblegame(d,R,PR,B,PB):
    print(d)
    print(R,B)
    # for b in board:
    #     print(''.join(b))
    if d > 10:
        return -1
    elif R == O:
        return d
    # 4방향으로 DFS
    for o in range(len(offset)):
        nr = move(o,R)
        if board[rn[0]][rn[1]] != '#':
            if rn == B:
                moveB()
            R,PR,Rn = rn,R,PR
            B,PB,bn = bn,B,PB
            marblegame(nd,o)
            R,PR,Rn = PR,rn,R
            B,PB,bn = PB,bn,B

def getnext(o,R,B):
    while :

    return

if __name__ == '__main__':
    N,M = map(int,stdin.readline().split())
    board = [list(stdin.readline().strip()) for _ in range(N)]
    R,B = [],[]
    res = -1

    for i in range(N):
        if R and B: break;
        for j in range(M):
            if board[i][j] == 'R':
                R = [i,j]
                board[i,j] == '.'
            elif board[i][j] == 'B':
                B = [i,j]
                board[i,j] == '.'

    marblegame(0,R,B)
    print(res)
