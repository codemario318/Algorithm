n = 4
works =[4,3,3]

# def solution1(n, works):
#     if sum(works) < n:
#         return 0
#     for _ in range(n):
#         if sum(works) == 0:
#             return 0
#         works.sort(reverse=True)
#         works[0]-=1
#     return sum(map(lambda x: x**2,works))

# def solution1(n, works):
#     if sum(works) < n:
#         return 0
#     cnt = n
#     while(cnt > 0):
#         if sum(works) == 0:
#             return 0
#         works.sort(reverse=True)
#         max_val = works[0]
#         for i in range(len(works)):
#             if works[i] == max_val and cnt > 0:
#                 works[i] -= 1
#                 cnt -=1
#             else:
#                 break
#     return sum(map(lambda x: x**2,works))
# solution1(n,works)
import bisect
bisect.bisect_right(works,works[0],rev)


from itertools import combinations
def solution(n, works):
    if sum(works) < n:
        return 0
    for _ in range(n):
        if sum(works) == 0:
            return 0
        i,_ = max(enumerate(works),key=lambda x:x[1])
        works[i] -= 1

    return sum(map(lambda x: x**2,works))

solution1(n,works)
