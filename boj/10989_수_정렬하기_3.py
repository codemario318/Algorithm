from sys import stdin

cnt = int(stdin.readline())

nums = {}

while(cnt > 0):
	num = int(stdin.readline())
	try:
		nums[num] += 1
	except KeyError:
		nums[num] = 1
	cnt -= 1

for k in sorted(nums.keys()):
	print((str(k)+'\n')*(nums[k]-1)+str(k))



#
# cnt = int(input())
#
# nums = {}
#
# while(cnt > 0):
# 	num = int(input())
# 	try:
# 		nums[num] += 1
# 	except KeyError:
# 		nums[num] = 1
# 	cnt -= 1
#
# for k in sorted(nums.keys()):
# 	print((str(k)+'\n')*(nums[k]-1)+str(k))
