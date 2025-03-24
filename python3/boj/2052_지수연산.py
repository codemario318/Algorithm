'''
지수연산

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	8 MB	4149	1364	1215	39.525%
문제
양의 정수
$N$이 주어질 때,

$\displaystyle\frac{1}{2^N}$을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 정수
$N$이 주어진다.

출력
첫째 줄에

$\displaystyle\frac{1}{2^N}$의 정확한 값을 소수 형태로 출력한다. 단, 뒤에 불필요한
$0$을 덧붙여서는 안 된다.

제한
 
$1 ≤ N ≤ 250$ 
예제 입력 1
5
예제 출력 1
0.03125
출처
문제를 다시 작성한 사람: doju
'''
from sys import stdin

readline = stdin.readline

if __name__ == '__main__':
    N = int(readline())

    result = '0.'
    numerator = 1
    denominator = 2 ** N

    for _ in range(N):
        numerator *= 10
        digit, numerator = divmod(numerator, denominator)
        result += str(digit)

    print(result)
