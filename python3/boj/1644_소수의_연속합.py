'''
소수의 연속합 출처다국어
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	16306	7066	4967	42.569%
문제
하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.
3 : 3 (한 가지)
41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
53 : 5+7+11+13+17 = 53 (두 가지)
하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.
자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.
입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)
출력
첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.
예제 입력 1 
20
예제 출력 1 
0
예제 입력 2 
3
예제 출력 2 
1
예제 입력 3 
41
예제 출력 3 
3
예제 입력 4 
53
예제 출력 4 
2
출처
ICPC > Regionals > Asia Pacific > Japan > Asia Regional Contest 2005 in Tokyo A번
문제를 번역한 사람: author5
문제의 오타를 찾은 사람: d252b
데이터를 추가한 사람: thesulks
'''


def get_primes(n):
    sieve = [False for _ in range(n + 1)]

    for i in range(2, n + 1):
        if i**2 > n:
            break

        if not sieve[i]:
            for j in range(i**2, n + 1, i):
                sieve[j] = True

    return [i for i in range(2, n + 1) if not sieve[i]]


def prime_seq_sum(n, primes):
    count = 0
    total = 0
    left, right = 0, 0

    while True:
        if total < n:
            if right == len(primes):
                break
            total += primes[right]
            right += 1
        else:
            total -= primes[left]
            left += 1

        if total == n:
            count += 1

    return count


def main():
    N = int(input())

    primes = get_primes(N)
    res = prime_seq_sum(N, primes)
    print(res)


if __name__ == '__main__':
    main()
