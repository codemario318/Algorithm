'''
이항 계수 1
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	9849	6184	5341	64.411%
문제
자연수 과 정수 가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

출력
 를 출력한다.
'''
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

n,k = map(int,input().split())
print(int(factorial(n)/(factorial(k)*factorial(n-k))))
