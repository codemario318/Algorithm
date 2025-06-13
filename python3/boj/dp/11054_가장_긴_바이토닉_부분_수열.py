'''
가장 긴 바이토닉 부분 수열

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	61567	31846	24915	51.322%
문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만, {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

예제 입력 1
10
1 5 2 1 4 3 4 5 2 1
예제 출력 1
7
힌트
예제의 경우 {1 5 2 1 4 3 4 5 2 1}이 가장 긴 바이토닉 부분 수열이다.

출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: gmldk728, kisu9454, sungbin95
문제의 오타를 찾은 사람: mwy3055
비슷한 문제
11053번. 가장 긴 증가하는 부분 수열
11055번. 가장 큰 증가하는 부분 수열
11722번. 가장 긴 감소하는 부분 수열
12015번. 가장 긴 증가하는 부분 수열 2
12738번. 가장 긴 증가하는 부분 수열 3
14002번. 가장 긴 증가하는 부분 수열 4
14003번. 가장 긴 증가하는 부분 수열 5
'''
from sys import stdin

readline = stdin.readline


def get_lis(N, nums):
    mem = [1 for _ in range(N)]

    for i in range(1, N):
        for j in range(0, i):
            if nums[i] > nums[j] and mem[i] < mem[j] + 1:
                mem[i] = mem[j] + 1

    return mem


def get_lds(N, nums):
    mem = [1 for _ in range(N)]

    for i in range(N - 2, -1, -1):
        for j in range(N - 1, i, -1):
            if nums[i] > nums[j] and mem[i] < mem[j] + 1:
                mem[i] = mem[j] + 1

    return mem


if __name__ == '__main__':
    N = int(readline())
    nums = list(map(int, readline().split()))

    lis = get_lis(N, nums)
    lds = get_lds(N, nums)

    print(max(map(sum, zip(lis, lds))) - 1)
