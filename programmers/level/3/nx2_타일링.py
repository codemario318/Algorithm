def solution(n):
    cache = [0,1,2,3,5]

    for i in range(5,n+1):
        cache.append(cache[-1]+cache[-2]%1,000,000,007)
    return cache[n]

solution(15)
