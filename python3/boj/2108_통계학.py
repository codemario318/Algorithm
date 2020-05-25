from collections import Counter
from sys import stdin

# cnt = int(stdin.readline())
cnt = int(input())

nums = []

while(cnt > 0):
    # nums.append(int(stdin.readline()))
    nums.append(int(input()))
    cnt -= 1

nums.sort()
counter = Counter(nums)
common_nums = [ num for num,cnt in counter.items() if cnt == counter.most_common(1)[0][1]]
common_nums.sort(reverse=True)

print(round(sum(nums)/len(nums)))
print(nums[len(nums)//2])
if len(common_nums) < 2:
    print(common_nums[0])
else:
    print(common_nums[-2])
print(nums[-1]-nums[0])
