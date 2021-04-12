'''
소수 찾기 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	68245	32141	26368	48.205%
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1 
4
1 3 5 7
예제 출력 1 
3
출처
데이터를 추가한 사람: bclim9108, nova9128
문제의 오타를 찾은 사람: djm03178
'''
from sys import stdin
from math import sqrt

readline = stdin.readline
N = 1000
SQRT_N = 100


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    count = 0

    _ = readline()
    nums = map(int, readline().split())
    primes = [n for n in range(SQRT_N) if is_prime(n)]

    sieve = [True for _ in range(N+1)]

    sieve[0] = False
    sieve[1] = False

    for prime in primes:
        for i in range(prime*2, N+1, prime):
            sieve[i] = False

    for num in nums:
        count += sieve[num]

    print(count)
