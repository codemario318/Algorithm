'''
최대공약수와 최소공배수 출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	37636	22429	18364	62.484%
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

예제 입력 1 
24 18
예제 출력 1 
6
72
출처
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2004 > 중등부 1번

Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2004 > 고등부 1번

데이터를 추가한 사람: circlecho, jsh587
'''
from sys import stdin
readline = stdin.readline


def get_factors(n):
    return set([i for i in range(1, n+1) if not n % i])


if __name__ == '__main__':
    a, b = map(int, readline().split())

    a_factors = get_factors(a)
    b_factors = get_factors(b)

    common_factors = a_factors & b_factors

    gcd = max(common_factors)
    lcm = (a * b) // gcd

    print(gcd)
    print(lcm)
