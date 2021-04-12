'''
소수 출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	47791	18642	16191	39.433%
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1 
60
100
예제 출력 1 
620
61
예제 입력 2 
64
65
예제 출력 2 
-1
출처
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > 중등부 1번

데이터를 추가한 사람: hchanhong, kyaryunha
문제의 오타를 찾은 사람: jh05013, sky1357
잘못된 데이터를 찾은 사람: myungwoo
'''
from math import sqrt
from sys import stdin

readline = stdin.readline

MAX = 10000


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if not num % i:
            return False
    return True


def get_sieve(num):
    sqrt_num = sqrt(num)

    sieve = [True for i in range(num+1)]
    sieve[0] = False
    sieve[1] = False

    primes = [i for i in range(2, int(sqrt_num)) if is_prime(i)]

    for prime in primes:
        for i in range(prime*2, num+1, prime):
            sieve[i] = False

    return sieve


if __name__ == '__main__':
    n = int(readline())
    m = int(readline())

    sieve = get_sieve(MAX)

    primes = [i for i in range(n, m+1) if sieve[i]]

    if primes:
        print(sum(primes))
        print(min(primes))
    else:
        print(-1)
