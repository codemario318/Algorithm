'''
책 페이지 실패

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	22149	7389	5998	42.812%
문제
지민이는 전체 페이지의 수가 N인 책이 하나 있다. 첫 페이지는 1 페이지이고, 마지막 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.

입력
첫째 줄에 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 공백으로 구분해 출력한다.

예제 입력 1
11
예제 출력 1
1 4 1 1 1 1 1 1 1 1
예제 입력 2
7
예제 출력 2
0 1 1 1 1 1 1 1 0 0
예제 입력 3
19
예제 출력 3
1 12 2 2 2 2 2 2 2 2
예제 입력 4
999
예제 출력 4
189 300 300 300 300 300 300 300 300 300
예제 입력 5
543212345
예제 출력 5
429904664 541008121 540917467 540117067 533117017 473117011 429904664 429904664 429904664 429904664
출처
문제를 번역한 사람: baekjoon
'''
from sys import stdin

readline = stdin.readline


def solution(n):
    count = [0] * 10
    digit = 1

    while digit <= n:
        high = n // (digit * 10)
        cur = (n // digit) % 10
        low = n % digit

        for d in range(10):
            if d < cur:
                count[d] += (high + 1) * digit
            elif d == cur:
                count[d] += high * digit + (low + 1)
            else:
                count[d] += high * digit

        count[0] -= digit
        digit *= 10

    return count


if __name__ == '__main__':
    N = int(readline())
    print(*solution(N))
