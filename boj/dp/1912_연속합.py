'''
연속합
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	48126	13215	9124	27.114%
문제
n개의 정수로 이루어진 임의의 수열이 주어진다.
우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자.
여기서 정답은 12+21인 33이 정답이 된다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력 1
33
출처
데이터를 추가한 사람: djm03178 dohyeokkim doju kimdr123
빠진 조건을 찾은 사람: isac322 Qwaz
문제의 오타를 찾은 사람: jh05013
잘못된 데이터를 찾은 사람: tncks0121
'''
# n = 11
# nums = [10, -4,3,1,5, 6, -21, -2, 12, 21, -1]
#
# n = int(input())
# nums = list(map(int,input().split()))
#
# mem = [nums[0]]
# temp = nums[0]
#
# for i in range(1,n):
#     mem.append(max(mem[-1]+nums[i],nums[i]))
#     temp = max(mem[-1],temp)
#
# print(temp)

###############################################################################
def search(nums):
    if max(nums) <= 0:
        return max(nums)

    sum = 0
    temp = 0

    for n in nums:
    	sum += n
    	if sum < 0:
    		sum = 0
    	if temp < sum:
    		temp = sum
    return temp

_ = input()
print(search(list(map(int,input().split()))))
