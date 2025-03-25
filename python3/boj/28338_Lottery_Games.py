'''
Lottery Games 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	32	16	12	46.154%
문제
You live in a lively town named Lottery Vegas where lots of different kinds of lottery games are available for you to play. Next to your house, you found an interesting lottery game that is called Double ticket winner ainu7 for the win, named after a really famous Miku-admirer.

The ainu7 lottery game consists of
$P$ different lottery tickets. The i-th ticket contains numbers between
$1$ and
$N_i$, inclusive, and you are to pick
$M_i$ numbers out of them. The ainu7 lottery game seller also picks
$M_i$ numbers while you are picking. For each lottery ticket, you win if you and the seller have at least
$K_i$ numbers in common with the seller. You can assume that the seller picks the numbers at random, regardless of what you pick.

You are curious which of the
$P$ tickets gives you the highest winning odds. If there are multiple such tickets with the same highest winning odds, you want to know them all.

입력
The input consists of
$T$ test cases. The number of test cases
$T$ is given in the first line of the input.

The first line of each test case contains a single integer
$P$ (
$2 ≤ P ≤ 100$), the number of lottery tickets. Following
$P$ lines contains three numbers each:
$N_i$,
$M_i$, and
$K_i$ where
$3 ≤ N_i ≤ 50$,
$1 ≤ M_i ≤ N_i$, and
$1 ≤ K_i ≤ M_i$.

출력
For each test case, you must output a single line of integer(s). It must contain the lottery game number(s) with highest winning odds. If there are multiple, you must sort them, and the game number is 1-based.

예제 입력 1
2
4
3 1 1
8 2 1
8 4 2
8 3 1
7
8 7 1
8 7 2
8 7 3
8 7 4
8 7 5
8 7 6
8 7 7
예제 출력 1
4
1 2 3 4 5 6
출처
University > 전국 대학생 프로그래밍 대회 동아리 연합 > UCPC 2011 J번

문제를 만든 사람: haden
'''
from math import comb
from sys import stdin

readline = stdin.readline


def calc(n, m, k):
    # 확률 계산을 위한 변수
    total_outcomes = 0  # 전체 가능한 경우의 수
    favorable_outcomes = 0  # 당첨되는 경우의 수

    # 당신이 M개의 숫자를 선택하는 방법은 한 가지로 고정됨
    # 판매자가 M개의 숫자를 선택하는 모든 가능한 방법: C(N, M)
    total_outcomes = comb(n, m)

    # 당첨되는 경우: 당신과 판매자의 선택 중 적어도 K개가 일치하는 경우
    # i는 일치하는 숫자의 개수 (K부터 M까지)
    for i in range(k, m + 1):
        # 당신이 선택한 M개 중 i개를 판매자가 선택하는 방법: C(M, i)
        # 나머지 (M-i)개를 남은 (N-M)개 중에서 선택하는 방법: C(N-M, M-i)
        favorable_outcomes += comb(m, i) * comb(n - m, m - i)

    # 당첨 확률 계산
    return favorable_outcomes / total_outcomes


if __name__ == '__main__':
    T = int(readline())

    for _ in range(T):
        P = int(readline())

        probabilities = [calc(*map(int, readline().split())) for _ in range(P)]
        max_probability = max(probabilities)

        result = [str(i) for i, prob in enumerate(probabilities, 1) if prob == max_probability]

        print(' '.join(result))
