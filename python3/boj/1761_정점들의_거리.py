'''
정점들의 거리
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	7578	3110	1940	39.327%
문제
N(2 ≤ N ≤ 40,000)개의 정점으로 이루어진 트리가 주어지고 M(1 ≤ M ≤ 10,000)개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.

입력
첫째 줄에 노드의 개수 N이 입력되고 다음 N-1개의 줄에 트리 상에 연결된 두 점과 거리를 입력받는다. 그 다음 줄에 M이 주어지고, 다음 M개의 줄에 거리를 알고 싶은 노드 쌍이 한 줄에 한 쌍씩 입력된다. 두 점 사이의 거리는 10,000보다 작거나 같은 자연수이다.

정점은 1번부터 N번까지 번호가 매겨져 있다.

출력
M개의 줄에 차례대로 입력받은 두 노드 사이의 거리를 출력한다.

예제 입력 1 
7
1 6 13
6 3 9
3 5 7
4 1 3
2 4 20
4 7 2
3
1 6
1 4
2 6
예제 출력 1 
13
3
36
출처
문제를 번역한 사람: author6
문제의 오타를 찾은 사람: justin0907, wjsqjawns
빠진 조건을 찾은 사람: ntopia
'''
from sys import stdin
from heapq import heappop, heappush

readline = stdin.readline


def search(tree, a, b):
    D = [float('inf') for _ in range(len(tree))]
    hq = [(0, a)]

    D[a] = 0

    while hq:
        total, cur = heappop(hq)

        if cur == b:
            return total

        for nxt, cost in tree[cur].items():
            if D[nxt] > total + cost:
                D[nxt] = total + cost
                heappush(hq, (D[nxt], nxt))


def main():
    N = int(readline())
    tree = [{} for _ in range(N + 1)]

    for _ in range(N - 1):
        s, e, c = map(int, readline().split())
        tree[s][e] = c
        tree[e][s] = c

    M = int(readline())

    for _ in range(M):
        s, e = map(int, readline().split())
        print(search(tree, s, e))


if __name__ == '__main__':
    main()
