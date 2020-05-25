from sys import stdin

def sudoku(idx):
    if len(emptys) == idx:
        for b in board:
            print(' '.join(map(str,b)))
        exit()

    x, y = emptys[idx]

    for c in range(1,10):
        if col[x][c] or row[y][c] or sqr[x//3][y//3][c]: continue
        board[x][y] = c
        setcheck(True,x,y,c)
        sudoku(idx+1)
        board[x][y] = 0
        setcheck(False,x,y,c)

def setcheck(s,x,y,c):
    col[x][c] = s
    row[y][c] = s
    sqr[x//3][y//3][c] = s

if __name__ == "__main__":
    board = [list(map(int,stdin.readline().split())) for _ in range(9)]
    col = [[False for _ in range(10)] for _ in range(9)]
    row = [[False for _ in range(10)] for _ in range(9)]
    sqr = [[[False for _ in range(10)] for _ in range(3)] for _ in range(3)]

    emptys = []

    for i in range(9):
        for j in range(9):
            n = board[i][j]
            if n == 0:
                emptys.append((i,j))
            else:
                col[i][n] = True
                row[j][n] = True
                sqr[i//3][j//3][n] = True

    sudoku(0)
