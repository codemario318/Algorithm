# 10 20 30 40 50 40 25 10 # 8
# 1 2 3 2 1 2 3 2 1 # 5
from sys import stdin

def lis(n):
    if lisr[n] > 0:
        return lisr[n]
    else:
        temp = 1
        for i in range(n):
            if nums[n] > nums[i]:
                temp = max(temp, lis(i)+1)
        lisr[n] = temp
        return lisr[n]

def lds(n):
    if ldsr[n] > 0:
        return ldsr[n]
    else:
        temp = 1
        for i in range(N-1,n,-1):
            if nums[n] > nums[i]:
                temp = max(temp, lds(i)+1)
        ldsr[n] = temp
        return ldsr[n]

def lbs():
    res = 1

    for i in range(1,N-1):
        lbsr[i] = lis(i) + lds(i) -1
        res = max(res,lbsr[i])

    return res

if __name__ == '__main__':
    global N
    N = int(stdin.readline())
    nums = list(map(int,stdin.readline().split()))
    lisr = [0 for _ in range(N)]
    ldsr = [0 for _ in range(N)]
    lbsr = [0 for _ in range(N)]

    lisr[0] = 1
    ldsr[-1] = 1

    print(lbs())
    print(lisr)
    print(ldsr)
    print(lbsr)
