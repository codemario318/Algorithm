'''
최솟값과 최댓값 분류
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	192 MB	12702	5966	4291	50.082%
문제
N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수, 또는 제일 큰 정수를 찾는 것은 어려운 일이 아니다. 하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다. 이 문제를 해결해 보자.

여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최소, 최댓값을 찾아야 한다. 각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.

입력
첫째 줄에 N, M이 주어진다. 다음 N개의 줄에는 N개의 정수가 주어진다. 다음 M개의 줄에는 a, b의 쌍이 주어진다.

출력
M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 최솟값, 최댓값 순서로 출력한다.

예제 입력 1 
10 4
75
30
100
38
50
51
52
20
81
5
1 10
3 5
6 9
8 10
예제 출력 1 
5 100
38 100
20 81
5 81
'''
# from sys import stdin
# from math import ceil, log2
# readline = stdin.readline

# def init(node, start, end):
#     if start == end:
#         tree[node] = [arr[start], arr[start]]
#     else:
#         mid = (start + end) // 2
#         small_a, big_a = init(node * 2, start, mid)
#         small_b, big_b = init(node * 2 + 1, mid + 1, end)
#         tree[node] = [min(small_a, small_b), max(big_a, big_b)]
#     return tree[node]

# def interval_min_max(node, start, end, left, right):
#     if start > right or end < left:
#         return [float('inf'), 0]

#     if start >= left and end <= right:
#         return tree[node]
#     else:
#         mid = (start + end) // 2
#         small_a, big_a = interval_min_max(node * 2, start, mid, left, right)
#         small_b, big_b = interval_min_max(node * 2 + 1, mid + 1, end, left, right)
#         return min(small_a, small_b), max(big_a, big_b)

# N, M = map(int, readline().split())
# arr = [0] + [int(readline()) for _ in range(N)]
# h = int(ceil(log2(N))) + 1
# tree = [[0, 0] for _ in range(1 << h)]

# init(1, 1, N)

# for _ in range(M):
#     a, b = map(int, readline().split())
#     print(*interval_min_max(1, 1, N, a, b))

from sys import stdin

readline = stdin.readline


def interval_min_max(l, r):
    l += N
    r += N
    min_val, max_val = float('inf'), 0

    while l < r:
        if l & 1:
            if min_tree[l] < min_val:
                min_val = min_tree[l]
            if max_tree[l] > max_val:
                max_val = max_tree[l]
            l += 1

        if r & 1:
            r -= 1
            if min_tree[r] < min_val:
                min_val = min_tree[r]
            if max_tree[r] > max_val:
                max_val = max_tree[r]

        l >>= 1
        r >>= 1

    return min_val, max_val


N, M = map(int, readline().split())

min_tree = [0] * N
max_tree = [0] * N

for _ in range(N):
    num = int(readline())
    min_tree.append(num)
    max_tree.append(num)

for i in range(N - 1, 0, -1):
    min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1])
    max_tree[i] = max(max_tree[2 * i], max_tree[2 * i + 1])

for _ in range(M):
    a, b = map(int, readline().split())
    print(*interval_min_max(a - 1, b))
