## 만들수 있는 소수의 수
nums = [1, 2, 7, 6, 4]
from itertools import combinations

def solution(nums):
    cnt = 0
    # list(combinations(nums,3))
    for comb in combinations(nums,3):
        if sum(comb)%2 == 1:
            print(comb)
            cnt += 1

    return cnt
solution(nums)
