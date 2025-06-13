'''
계단 수

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	15494	8260	6279	52.805%
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N이면서 0부터 9까지 숫자가 모두 등장하는 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1
10
예제 출력 1
1
힌트
참고로, N=1일때부터, N=40일 때 까지 답을 모두 더하면 126461847755이 나온다.
'''

from sys import stdin

readline = stdin.readline
MOD = 1_000_000_000
BITMASK = 1024
DIGITS = 10

def solution(n):
    dp = [[[0 for _ in range(BITMASK)] for _ in range(DIGITS)] for _ in range(n + 1)]

    for i in range(1, DIGITS):
        dp[1][i][1 << i] = 1

    for length in range(2, n + 1):
        for digit in range(DIGITS):
            for prev_digit in [digit - 1, digit + 1]:
                if prev_digit < 0 or prev_digit >= DIGITS:
                    continue

                for bitmask in range(BITMASK):
                    new_mask = bitmask | (1 << digit)
                    dp[length][digit][new_mask] += dp[length - 1][prev_digit][bitmask] % MOD

    result = 0

    for digit in range(DIGITS):
        result = (result + dp[n][digit][BITMASK - 1]) % MOD

    return result

if __name__ == '__main__':
    N = int(readline())
    print(solution(N))
