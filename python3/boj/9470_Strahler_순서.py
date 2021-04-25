'''
Strahler 순서 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	1817	702	557	39.281%
문제
지질학에서 하천계는 유향그래프로 나타낼 수 있다. 강은 간선으로 나타내며, 물이 흐르는 방향이 간선의 방향이 된다. 노드는 호수나 샘처럼 강이 시작하는 곳, 강이 합쳐지거나 나누어지는 곳, 바다와 만나는 곳이다.



네모 안의 숫자는 순서를 나타내고, 동그라미 안의 숫자는 노드 번호를 나타낸다.

하천계의 Strahler 순서는 다음과 같이 구할 수 있다.

강의 근원인 노드의 순서는 1이다.
나머지 노드는 그 노드로 들어오는 강의 순서 중 가장 큰 값을 i라고 했을 때, 들어오는 모든 강 중에서 Strahler 순서가 i인 강이 1개이면 순서는 i, 2개 이상이면 순서는 i+1이다.
하천계의 순서는 바다와 만나는 노드의 순서와 같다. 바다와 만나는 노드는 항상 1개이며, 위의 그림의 Strahler 순서는 3이다.

하천계의 정보가 주어졌을 때, Strahler 순서를 구하는 프로그램을 작성하시오.

실제 강 중에서 Strahler 순서가 가장 큰 강은 아마존 강(12)이며, 미국에서 가장 큰 값을 갖는 강은 미시시피 강(10)이다.

노드 M은 항상 바다와 만나는 노드이다.

입력
첫째 줄에 테스트 케이스의 수 T (1 ≤ T ≤ 1000)가 주어진다.

각 테스트 케이스의 첫째 줄에는 K, M, P가 주어진다. K는 테스트 케이스 번호, M은 노드의 수, P는 간선의 수이다. (2 ≤ M ≤ 1000) 다음 P개 줄에는 간선의 정보를 나타내는 A, B가 주어지며, A에서 B로 물이 흐른다는 뜻이다. (1 ≤ A, B ≤ M) M은 항상 바다와 만나는 노드이며, 밖으로 향하는 간선은 존재하지 않는다.

출력
각 테스트 케이스마다 테스트 케이스 번호와 입력으로 주어진 하천계의 Strahler 순서를 한 줄에 하나씩 출력한다.

예제 입력 1 
1
1 7 8
1 3
2 3
6 4
3 4
3 5
6 7
5 7
4 7
예제 출력 1 
1 3
출처

1
1 9 8
1 3
2 3
4 6
5 6
3 9
6 9
7 8
8 9

ICPC > Regionals > North America > Greater New York Region > 2013 Greater New York Programming Contest C번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: djm03178, sait2000
문제의 오타를 찾은 사람: Hibbah, orihehe, sg1774, YunGoon
링크
ACM-ICPC Live Archive
'''
from sys import stdin
readline = stdin.readline


def solution(m, graph, starts):
    strahlers = [1 for _ in range(m+1)]
    visited = [False for _ in range(m+1)]
    q = list(starts)

    while q:
        cur = q.pop(0)
        strahler = strahlers[cur]

        for nxt in graph[cur]:
            if strahlers[nxt] < strahler:
                strahlers[nxt] = strahler
                visited[nxt] = False
                q.append(nxt)
            elif strahlers[nxt] == strahler:
                if not visited[nxt]:
                    strahlers[nxt] = strahler+1
                    visited[nxt] = True
                else:
                    visited[nxt] = False
                q.append(nxt)

    return strahlers[m]


def main():
    T = int(readline())

    for _ in range(T):
        K, M, P = map(int, readline().split())
        graph = [[] for _ in range(M+1)]
        starts = set([i for i in range(1, M+1)])

        for _ in range(P):
            s, e = map(int, readline().split())
            graph[s].append(e)

            if e in starts:
                starts.remove(e)

        print(K, solution(M, graph, starts))


if __name__ == '__main__':
    main()
