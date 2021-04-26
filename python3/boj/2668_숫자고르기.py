'''
숫자고르기 출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	7716	3298	2650	44.538%
문제
세로 두 줄, 가로로 N개의 칸으로 이루어진 표가 있다. 첫째 줄의 각 칸에는 정수 1, 2, …, N이 차례대로 들어 있고 둘째 줄의 각 칸에는 1이상 N이하인 정수가 들어 있다. 첫째 줄에서 숫자를 적절히 뽑으면, 그 뽑힌 정수들이 이루는 집합과, 뽑힌 정수들의 바로 밑의 둘째 줄에 들어있는 정수들이 이루는 집합이 일치한다. 이러한 조건을 만족시키도록 정수들을 뽑되, 최대로 많이 뽑는 방법을 찾는 프로그램을 작성하시오. 예를 들어, N=7인 경우 아래와 같이 표가 주어졌다고 하자.



이 경우에는 첫째 줄에서 1, 3, 5를 뽑는 것이 답이다. 첫째 줄의 1, 3, 5밑에는 각각 3, 1, 5가 있으며 두 집합은 일치한다. 이때 집합의 크기는 3이다. 만약 첫째 줄에서 1과 3을 뽑으면, 이들 바로 밑에는 정수 3과 1이 있으므로 두 집합이 일치한다. 그러나, 이 경우에 뽑힌 정수의 개수는 최대가 아니므로 답이 될 수 없다.

입력
첫째 줄에는 N(1≤N≤100)을 나타내는 정수 하나가 주어진다. 그 다음 줄부터는 표의 둘째 줄에 들어가는 정수들이 순서대로 한 줄에 하나씩 입력된다.

출력
첫째 줄에 뽑힌 정수들의 개수를 출력하고, 그 다음 줄부터는 뽑힌 정수들을 작은 수부터 큰 수의 순서로 한 줄에 하나씩 출력한다.

예제 입력 1
7
3
1
1
5
5
4
6
예제 출력 1
3
1
3
5
출처

3
3
1
2

4 
4
3
2
1

Olympiad > 한국정보올림피아드 > KOI 1996 > 초등부 2번

문제의 오타를 찾은 사람: eric00513
데이터를 추가한 사람: yysu1004
'''
from sys import stdin
readline = stdin.readline


def dfs(start, cur, nums, visited):
    visited[cur] = True

    nxt = nums[cur]

    if start == nxt:
        return True

    if not visited[nxt]:
        return dfs(start, nxt, nums, visited)

    return False


def main():
    n = int(readline())
    nums = [0] + [int(readline()) for _ in range(n)]
    used = [False for _ in range(n+1)]

    for i in range(1, n+1):
        if not used[i]:
            visited = used.copy()
            if dfs(i, i, nums, visited):
                used = visited

    res = [i for i in range(1, n+1) if used[i]]

    print(len(res))

    for r in res:
        print(r)


if __name__ == '__main__':
    main()
