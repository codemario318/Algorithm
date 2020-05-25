'''
2

2

9

55
'''
from collections import deque

if __name__ == "__main__":
    N = int(input())
    if N < 3:
        print(N)
    else:
        temp = deque([1,2],2)

        for _ in range(2,N):
            temp.append(sum(temp)%10007)

        print(temp[-1])
