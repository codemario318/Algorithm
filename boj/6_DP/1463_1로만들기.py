'''
1로 만들기
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	74255	24230	15492	32.095%
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

예제 입력 1
2
예제 출력 1
1
예제 입력 2
10
예제 출력 2
3
힌트
10의 경우에 10 -> 9 -> 3 -> 1 로 3번 만에 만들 수 있다.

출처
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: cyj101366 jugol
어색한 표현을 찾은 사람: dbfldkfdbgml
데이터를 추가한 사람: dynamiseus
'''
# from sys import setrecursionlimit
# setrecursionlimit(100000)
from sys import stdin

def dp(n):
    try:
        return costs[n]
    except KeyError:
        if n%6 == 0:
            temp = min(dp(n//2),dp(n//3))
        elif n%3 == 0:
            temp = min(dp(n//3),dp(n-1))
        elif n%2 == 0:
            temp = min(dp(n//2),dp(n-1))
        else:
            temp = dp(n-1)

        costs[n] = temp + 1
        return costs[n]

n = int(stdin.readline())
costs = {1:0,2:1,3:1}

print(dp(n))
