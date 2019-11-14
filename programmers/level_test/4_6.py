
from math import factorial as f

def solution(n):
    return f(2*n)/(f(n+1) * f(n))


solution(6,[1,2,3])
list(enumerate([1,2,3,]))
sorted(list(enumerate(1,[1,2,3])))
from heapq import heappop,heappush
from bisect import bisect_right
range()
def solution(n, cores):
    temp = sorted(enumerate(cores,1),key=lambda x:(x[1],x[0]))
    job = n -len(cores)
    q = []
    for _ in range(n-1):

        for i in range(len(cores)):
            if temp[i] == 0:
                temp[i] = cores[i]
                job -= 1
            if job == 0:
                return i+1
        temp = list(map(lambda x: x-1,temp))
