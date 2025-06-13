'''
N과 M (9)

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	52752	26463	20220	49.220%
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1
3 1
4 4 2
예제 출력 1
2
4
예제 입력 2
4 2
9 7 9 1
예제 출력 2
1 7
1 9
7 1
7 9
9 1
9 7
9 9
예제 입력 3
4 4
1 1 1 1
예제 출력 3
1 1 1 1
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: kid7ho
'''

from sys import stdin

readline = stdin.readline


def dfs(nums, selected, visited, limit):
    if len(selected) == limit:
        print(*selected)
        return

    prev = None

    for i in range(len(nums)):
        if visited[i] or prev == nums[i]:
            continue

        selected.append(nums[i])
        visited[i] = True
        dfs(nums, selected, visited, limit)
        selected.pop()
        visited[i] = False
        prev = nums[i]


if __name__ == '__main__':
    N, M = map(int, readline().split())
    nums = sorted(map(int, readline().split()))

    dfs(nums, [], [False] * N, M)
