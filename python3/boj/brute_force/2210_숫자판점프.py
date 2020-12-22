'''
숫자판 점프 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	3215	2380	1862	73.163%
문제
5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.

숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.

입력
다섯 개의 줄에 다섯 개의 정수로 숫자판이 주어진다.

출력
첫째 줄에 만들 수 있는 수들의 개수를 출력한다.

예제 입력 1 
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1
예제 출력 1 
15
힌트
111111, 111112, 111121, 111211, 111212, 112111, 112121, 121111, 121112, 121211, 121212, 211111, 211121, 212111, 212121 이 가능한 경우들이다.
'''
from sys import stdin

N = 5
OFFSET = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def readline():
    return map(int, stdin.readline().split())


def dfs(arr, i, j, num):
    if len(num) == N+1:
        global res
        res.add(''.join(map(str, num)))
    else:
        for wi, wj in OFFSET:
            ni, nj = i+wi, j+wj
            nxt = (ni, nj)
            if 0 <= ni < N and 0 <= nj < N:
                num.append(arr[ni][nj])
                dfs(arr, ni, nj, num)
                num.pop()


if __name__ == "__main__":
    global res
    res = set()
    nums = [list(readline()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dfs(nums, i, j, [nums[i][j]])

    print(len(res))
