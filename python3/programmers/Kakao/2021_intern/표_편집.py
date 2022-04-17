def solution(n, k, cmd):
    sheet = ['O' for _ in range(n)]
    deleted = []
    pos = 0

    for s in cmd:
        c, *x = s.split()

        if c == 'U':
            pos = move(c, int(x[0]))
        elif c == 'D':
            pos = move(c, -int(x[0]))
        elif c == 'C':
            remove(sheet, pos)


    return answer


    a, *b = 'a'.split()
    b