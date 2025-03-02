'''
제곱수의 합

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	67419	27723	20230	40.211%
문제
어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 예를 들어 11=32+12+12(3개 항)이다. 이런 표현방법은 여러 가지가 될 수 있는데, 11의 경우 11=22+22+12+12+12(5개 항)도 가능하다. 이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

출력
주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.

예제 입력 1
7
예제 출력 1
4
예제 입력 2
1
예제 출력 2
1
예제 입력 3
4
예제 출력 3
1
예제 입력 4
11
예제 출력 4
3
예제 입력 5
13
예제 출력 5
2
출처
ICPC > Regionals > Asia Pacific > Korea > Nationwide Internet Competition > Seoul Nationalwide Internet Competition 2007 E번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: godmoon00
데이터를 추가한 사람: sbukkk, yukariko
'''

from sys import stdin

readline = stdin.readline

# 라그랑주의 네 제곱수 정리에 의해, 모든 자연수는 최대 4개의 제곱수 합으로 표현 가능
def min_square_sum(n):
    # 제곱수인 경우 1 반환
    if int(n ** 0.5) ** 2 == n:
        return 1

    # 두 제곱수의 합으로 표현 가능한지 확인
    for i in range(1, int(n ** 0.5) + 1):
        if int((n - i ** 2) ** 0.5) ** 2 == n - i ** 2:
            return 2

    # n = 4^k * (8*m + 7) 형태인지 확인 (이 경우 항상 4개의 제곱수 필요)
    temp = n
    while temp % 4 == 0:
        temp //= 4
    if temp % 8 == 7:
        return 4

    # 그 외의 경우는 모두 3개의 제곱수로 표현 가능
    return 3


if __name__ == '__main__':
    N = int(readline())
    print(min_square_sum(N))
