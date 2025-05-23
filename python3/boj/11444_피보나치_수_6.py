'''
피보나치 수 6

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	28726	12908	10681	47.647%
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.

예제 입력 1
1000
예제 출력 1
517691607
출처
문제를 만든 사람: baekjoon
'''

from sys import stdin

readline = stdin.readline
MOD = 10 ** 9 + 7


def matrix_multiply(A, B):
    C = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C


def matrix_power(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        half_pow = matrix_power(A, n // 2)
        return matrix_multiply(half_pow, half_pow)
    else:
        return matrix_multiply(A, matrix_power(A, n - 1))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    A = [[1, 1], [1, 0]]
    result_matrix = matrix_power(A, n - 1)
    return result_matrix[0][0]


if __name__ == '__main__':
    n = int(readline())
    print(fibonacci(n))
