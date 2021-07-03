'''
가장 긴 증가하는 부분 수열 2
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	16369	6667	4660	44.276%
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: harinboy, jh05013, surung9898, tony9402
비슷한 문제
11053번. 가장 긴 증가하는 부분 수열
11054번. 가장 긴 바이토닉 부분 수열
11055번. 가장 큰 증가 부분 수열
11722번. 가장 긴 감소하는 부분 수열
12738번. 가장 긴 증가하는 부분 수열 3
14002번. 가장 긴 증가하는 부분 수열 4
14003번. 가장 긴 증가하는 부분 수열 5
'''
from sys import stdin
from bisect import bisect_left

readline = stdin.readline

_ = int(readline())
nums = map(int, readline().split())
mem = [next(nums)]

for num in nums:
    if mem[-1] < num:
        mem.append(num)
    else:
        i = bisect_left(mem, num)
        mem[i] = num
        
print(len(mem))