'''
피리 부는 사나이

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	11786	5392	4043	42.756%
문제
피리 부는 사나이 성우는 오늘도 피리를 분다.

성우가 피리를 불 때면 영과일 회원들은 자기도 모르게 성우가 정해놓은 방향대로 움직이기 시작한다. 성우가 정해놓은 방향은 총 4가지로 U, D, L, R이고 각각 위, 아래, 왼쪽, 오른쪽으로 이동하게 한다.

이를 지켜보던 재훈이는 더 이상 움직이기 힘들어하는 영과일 회원들을 지키기 위해 특정 지점에 ‘SAFE ZONE’ 이라는 최첨단 방음 시설을 만들어 회원들이 성우의 피리 소리를 듣지 못하게 하려고 한다. 하지만 예산이 넉넉하지 않은 재훈이는 성우가 설정해 놓은 방향을 분석해서 최소 개수의 ‘SAFE ZONE’을 만들려 한다.

성우가 설정한 방향 지도가 주어졌을 때 재훈이를 도와서 영과일 회원들이 지도 어느 구역에 있더라도 성우가 피리를 불 때 ‘SAFE ZONE’에 들어갈 수 있게 하는 ‘SAFE ZONE’의 최소 개수를 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에 지도의 행의 수를 나타내는 N(1 ≤ N ≤ 1,000)과 지도의 열의 수를 나타내는 M(1 ≤ M ≤ 1,000)이 주어진다.

두 번째 줄부터 N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열이 주어진다.

지도 밖으로 나가는 방향의 입력은 주어지지 않는다.

출력
첫 번째 줄에 ‘SAFE ZONE’의 최소 개수를 출력한다.

예제 입력 1
3 4
DLLL
DRLU
RRRU
예제 출력 1
2


예제 입력 1
3 4
DLLL
DLLU
RRRU
예제 출력 1
1


다음과 같이 'SAFE ZONE'을 만들면 영과일 회원들이 지도 어느 구역에 있더라도 'SAFE ZONE'에 들어갈 수 있다.

출처
University > 한양대학교 ERICA 캠퍼스 > Zero One Algorithm Contest 2018 F번

문제를 만든 사람: hellogaon
'''
from collections import deque
from sys import stdin

readline = stdin.readline
OFFSET = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def find(parent, pos):
    i, j = pos
    if parent[i][j] != pos:
        parent[i][j] = find(parent, parent[i][j])
    return parent[i][j]


def union(parent, pos_a, pos_b):
    pos_a, pos_b = (ai, aj), (bi, bj) = find(parent, pos_a), find(parent, pos_b)

    if pos_a < pos_b:
        parent[bi][bj] = pos_a
    else:
        parent[ai][aj] = pos_b


def bfs(board, pos, parent):
    queue = deque([pos])

    while queue:
        cur = i, j = queue.popleft()
        wi, wj = OFFSET[board[i][j]]
        nxt = i + wi, j + wj

        if find(parent, cur) == find(parent, nxt):
            continue

        union(parent, cur, nxt)
        queue.append(nxt)


if __name__ == '__main__':
    N, M = map(int, readline().split())
    board = [readline().strip() for _ in range(N)]

    parent = [[(i, j) for j in range(M)] for i in range(N)]

    for i in range(N):
        for j in range(M):
            bfs(board, (i, j), parent)

    safe_zone = set()

    for i in range(N):
        for j in range(M):
            safe_zone.add(find(parent, (i, j)))

    print(len(safe_zone))
