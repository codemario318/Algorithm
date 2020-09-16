from collections import deque

def draw_snail(snail):
    index_check = lambda x: True if 0 <= x < N else False
    N = len(snail)
    offset = deque([(0,1),(1,0),(0,-1),(-1,0)])

    cur_x, cur_y = 0,0
    wx, wy = offset[0]
    count = 0

    while count < 2:
        next_x, next_y = cur_x + wx, cur_y + wy

        snail[cur_x][cur_y] = '#'

        if not index_check(next_x) or not index_check(next_y):
            offset.rotate(-1)
            wx, wy = offset[0]
            count += 1
        elif snail[next_x][next_y] == '#':
            snail[cur_x][cur_y] = ' '
            cur_x -= wx
            cur_y -= wy
            offset.rotate(-1)
            wx, wy = offset[0]
            count += 1
        else:
            count = 0
            cur_x,cur_y = next_x, next_y

    wx, wy = offset[-1]
    next_x,next_y = cur_x + wx, cur_y + wy
    snail[next_x][next_y] = '#'
    return ' \n'.join(map(' '.join,snail))

if __name__ == '__main__':
    n = int(input())

    snail = [[' ' for _ in range(n)] for _ in range(n)]
    print(draw_snail(snail))
