'''
음식물 피하기 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	5447	2533	2121	47.397%
문제
코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다. 

이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다. 

통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다. 

선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.

입력
첫째 줄에 통로의 세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 그리고 음식물 쓰레기의 개수 K(1 ≤ K ≤ 10,000)이 주어진다.  그리고 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.

좌표 (r, c)의 r은 위에서부터, c는 왼쪽에서부터가 기준이다.

출력
첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력하라.

예제 입력 1 
3 4 5
3 2
2 2
3 1
2 3
1 1
예제 출력 1 
4
힌트
# . . .
. # # .
# # . .
위와 같이 음식물이 떨어져있고 제일큰 음식물의 크기는 4가 된다. (인접한 것은 붙어서 크게 된다고 나와 있음. 대각선으로는 음식물 끼리 붙을수 없고 상하좌우로만 붙을수 있다.)

출처
Olympiad > USA Computing Olympiad > 2007-2008 Season > USACO November 2007 Contest > Bronze 3번

문제를 번역한 사람: author9
문제의 오타를 찾은 사람: eric00513
'''

from sys import stdin
from collections import deque

OFFSET = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def readline(): return map(int, stdin.readline().split())


def search(trash, N, M, s, visited):
    q = deque([s])
    cnt = 1

    while q:
        i, j = q.popleft()

        for wi, wj in OFFSET:
            ni, nj = i+wi, j+wj
            nxt = (ni, nj)

            if 0 < ni <= N and 0 < nj <= M and nxt in trash and nxt not in visited:
                cnt += 1
                visited.add(nxt)
                q.append(nxt)

    return cnt


if __name__ == '__main__':
    N, M, K = readline()
    trash = set(tuple(readline()) for _ in range(K))
    visited = set()
    res = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            cur = (i, j)
            if cur in trash and cur not in visited:
                visited.add(cur)
                res = max(res, search(trash, N, M, cur, visited))

    print(res)
