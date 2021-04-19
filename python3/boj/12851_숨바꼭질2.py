'''
숨바꼭질 2 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	15057	4132	2895	25.800%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
2

5 237
10
5
출처
문제를 만든 사람: baekjoon
비슷한 문제
1697번. 숨바꼭질
13549번. 숨바꼭질 3
13913번. 숨바꼭질 4
'''
from collections import deque

POS_MIN = 0
POS_MAX = 100000


def search(n, k):
    res, cnt = float('inf'), 0
    visited = [float('inf') for _ in range(POS_MAX + 1)]

    q = deque([(n, 0)])

    while q:
        cur, step = q.popleft()

        if step > res:
            continue

        if cur == k:
            if res > step:
                res = step
                cnt = 1
            else:
                cnt += 1

        if cur < POS_MAX and step <= visited[cur+1]:
            visited[cur+1] = step
            q.append((cur+1, step+1))

        if cur > POS_MIN and step <= visited[cur-1]:
            visited[cur-1] = step
            q.append((cur-1, step+1))

        if 0 < cur*2 <= POS_MAX and step <= visited[cur*2]:
            visited[cur*2] = step
            q.append((cur*2, step+1))

    return res, cnt


n, k = map(int, input().split())

res, cnt = search(n, k)

print(res)
print(cnt)
