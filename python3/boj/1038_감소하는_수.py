'''
감소하는 수 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	13410	3564	2836	30.283%
문제
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

입력
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 N번째 감소하는 수를 출력한다.

예제 입력 1 
18
예제 출력 1 
42
출처
문제를 번역한 사람: baekjoon
'''
from collections import deque

X = int(input())

nums = [0]

temp = deque(range(1, 10))

while len(nums)-1 < X:
    if not temp:
        print(-1)
        break

    n = temp.popleft()
    nums.append(n)

    s = n % 10
    n *= 10

    for i in range(s):
        temp.append(n+i)
else:
    print(nums[-1])
