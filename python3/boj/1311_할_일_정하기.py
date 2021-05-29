'''
할 일 정하기 1 분류
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	498	196	147	49.495%
문제
N명의 사람과 N개의 일이 있다. 각 사람은 일을 하나 담당해야 하고, 각 일을 담당하는 사람은 한 명 이어야 한다. 또한, 모든 사람은 모든 일을 할 능력이 있다.

사람은 1번부터 N번까지 번호가 매겨져 있으며, 일도 1번부터 N번까지 번호가 매겨져 있다.

Dij를 i번 사람이 j번 일을 할 때 필요한 비용이라고 했을 때, 모든 일을 하는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람과 일의 수 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 D의 내용이 주어진다. 비용은 10,000보다 작거나 같은 자연수이다.

출력
모든 일을 하는데 필요한 비용의 최솟값을 출력한다.

예제 입력 1 
3
2 3 3
3 2 3
3 3 2
예제 출력 1 
6
출처
문제를 만든 사람: baekjoon, xhark
'''
from sys import stdin

readline = stdin.readline


def dfs(p, worked):
    if worked == (1 << N) - 1:
        return 0

    if mem[p][worked] > 0:
        return mem[p][worked]

    mem[p][worked] = float('inf')

    for j in range(N):
        if worked & (1 << j):
            continue
        mem[p][worked] = min(mem[p][worked],
                             dfs(p + 1, worked | (1 << j)) + D[p][j])

    return mem[p][worked]


N = int(readline())
D = [list(map(int, readline().split())) for _ in range(N)]
mem = [[0 for _ in range((1 << N) - 1)] for _ in range(N)]

print(dfs(0, 0))