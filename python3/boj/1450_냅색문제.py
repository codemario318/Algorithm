'''
냅색문제 분류
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	2482	733	511	31.273%
문제
세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.

N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 C가 주어진다. N은 30보다 작거나 같은 자연수이고, C는 10^9보다 작거나 같은 음이아닌 정수이고. 둘째 줄에 물건의 무게가 주어진다. 무게도 10^9보다 작거나 같은 자연수이다.

출력
첫째 줄에 가방에 넣는 방법의 수를 출력한다.

예제 입력 1 
2 1
1 1
예제 출력 1 
3
출처
문제를 번역한 사람: baekjoon
'''
from bisect import bisect_right


def dfs(start, end, total, items):
    if total > C:
        return
    if start == end:
        items.append(total)
        return
    dfs(start + 1, end, total, items)
    dfs(start + 1, end, total + arr[start], items)


N, C = map(int, input().split())
arr = list(map(int, input().split()))

left = []
right = []

dfs(0, N // 2, 0, left)
dfs(N // 2, N, 0, right)

left.sort()
right.sort()

res = 0

for l in left:
    p = bisect_right(right, C - l)
    res += p

print(res)
