'''
공항 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	256 MB	26123	9449	7085	35.886%
문제
오늘은 신승원의 생일이다.

박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.

공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.

공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다. 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다. 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?

입력
첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.

두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.

이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.

출력
승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력한다.

예제 입력 1
4
3
4
1
1
예제 출력 1
2
예제 입력 2
4
6
2
2
3
3
4
4
예제 출력 2
3
힌트
예제 1 : [2][?][?][1] 형태로 도킹시킬 수 있다. 3번째 비행기는 도킹시킬 수 없다.

예제 2 : [1][2][3][?] 형태로 도킹 시킬 수 있고, 4번째 비행기는 절대 도킹 시킬 수 없어서 이후 추가적인 도킹은 불가능하다.



출처
Olympiad > Canadian Computing Competition & Olympiad > 2015 > CCC 2015 Senior Division 3번

문제의 오타를 찾은 사람: atagkim, jh05013
데이터를 추가한 사람: chan4928, queued_q
잘못된 번역을 찾은 사람: dlaud5379
문제를 번역한 사람: koosaga
'''

from sys import stdin

readline = stdin.readline


def find(parents, i):
    if parents[i] != i:
        parents[i] = find(parents, parents[i])
    return parents[i]


def union(parants, i, j):
    a, b = find(parants, i), find(parants, j)

    if a < b:
        parants[b] = a
    else:
        parants[a] = b


if __name__ == '__main__':
    G = int(readline())
    P = int(readline())
    planes = [int(readline()) for _ in range(P)]

    parents = [i for i in range(G + 1)]
    count = 0

    for g in planes:
        gate = find(parents, g)

        if gate == 0:
            break

        union(parents, gate, gate - 1)
        count += 1

    print(count)
