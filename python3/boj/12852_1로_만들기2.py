'''
1로 만들기 2 스페셜 저지
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초	512 MB	6111	2791	2314	49.276%
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 정답이 여러 가지인 경우에는 아무거나 출력한다.

예제 입력 1 
2
예제 출력 1 
1
2 1
예제 입력 2 
10
예제 출력 2 
3
10 9 3 1
출처
문제를 만든 사람: baekjoon
'''
from collections import deque

x = int(input())
costs = [float('inf') for _ in range(x + 1)]
prevs = [0 for _ in range(x + 1)]
q = deque([(x, 0)])

costs[x] = 0

while q:
    n, cost = q.popleft()

    if n == 1:
        break
    elif n < 1:
        continue

    if not n % 3 and costs[n // 3] > cost + 1:
        costs[n // 3] = cost + 1
        prevs[n // 3] = n
        q.append((n // 3, cost + 1))
    if not n % 2 and costs[n // 2] > cost + 1:
        costs[n // 2] = cost + 1
        prevs[n // 2] = n
        q.append((n // 2, cost + 1))
    if costs[n - 1] > cost + 1:
        costs[n - 1] = cost + 1
        prevs[n - 1] = n
        q.append((n - 1, cost + 1))

print(costs[1])
res = deque([1])

while res[0] != x:
    cur = res[0]
    res.appendleft(prevs[cur])

print(*res)
