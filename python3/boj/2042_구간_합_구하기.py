'''
구간 합 구하기 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	48060	9518	4898	23.548%
문제
어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 -2^63보다 크거나 같고, 2^63-1보다 작거나 같은 정수이다.

출력
첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -2^63보다 크거나 같고, 2^63-1보다 작거나 같은 정수이다.

예제 입력 1 
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
예제 출력 1 
17
12
출처
문제의 오타를 찾은 사람: 79brue, keunbum, Nyan101, tncks0121
빠진 조건을 찾은 사람: 79brue, djm03178, jh05013
데이터를 추가한 사람: klm03025
잘못된 조건을 찾은 사람: WeissBlume
'''
from sys import stdin

readline = stdin.readline


def update(tree, i, n):
    while i <= N:
        tree[i] += n
        i += (i & -i)


def prefix_sum(tree, i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res


def interval_sum(tree, s, e):
    return prefix_sum(tree, e) - prefix_sum(tree, s - 1)


N, M, K = map(int, readline().split())

arr = [0 for _ in range(N + 1)]
tree = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    n = int(readline())
    arr[i] = n
    update(tree, i, n)

for _ in range(M + K):
    mode, a, b = map(int, readline().split())

    if mode == 1:
        update(tree, a, b - arr[a])
        arr[a] = b
    else:
        print(interval_sum(tree, a, b))
