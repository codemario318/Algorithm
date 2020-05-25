'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

10
9
7
55
30
'''

from sys import stdin

def ox(s):
    res = 0
    cnt = 1
    for ans in s:
        if ans =="O":
            res += cnt
            cnt += 1
        else:
            cnt = 1
    return res

if __name__ == "__main__":
    N = int(stdin.readline())

    for _ in range(N):
        print(ox(stdin.readline().strip()))
