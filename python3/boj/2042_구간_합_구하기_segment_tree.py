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
from math import sqrt, ceil

readline = stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(
            node * 2 + 1, (start + end) // 2 + 1, end)
    return tree[node]


def interval_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return interval_sum(node * 2, start,
                        (start + end) // 2, left, right) + interval_sum(
                            node * 2 + 1,
                            (start + end) // 2 + 1, end, left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2, (start + end) // 2 + 1, end, index, diff)


N, M, K = map(int, readline().split())

# 세그먼트 트리 계산을 오류 없이 하기 위해 완전 이진 트리를 사용하며
# 리프 노드의 개수가 N개인 완전 이진 트리에 필요한 노드 수는
# 2**트리의 높이+1 이고 트리의 높이는 log2N 이다.

h = ceil(sqrt(N))
tree = [0 for _ in range(2**(h + 1))]
arr = list(map(int, readline().split()))

init(1, 0, N - 1)

for _ in range(M + K):
    mode, a, b = map(int, readline().split())

    if mode == 1:
        diff = b - arr[a]
        arr[a] = b
        update(1, 0, N - 1, a, diff)
    else:
        print(interval_sum(tree, a, b))
