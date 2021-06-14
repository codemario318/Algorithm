'''
수상 택시 출처다국어분류
 
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	1276	431	349	33.112%
문제
상근이가 살고 있는 도시에는 큰 강이 흐르고 있고, 모든 사람의 집은 이 강 근처에 있다. 집은 0번부터 M번까지 강을 따라서 번호가 매겨져 있고, 인접한 집 사이의 거리는 모두 1 킬로미터이다.

상근이는 0번 집에 살고 있고, 보트를 이용해서 사람들을 운송하는 일을 하고 있다.

오늘은 저녁때까지 M번 집으로 가야한다. 상근이는 M번 집으로 가는 길에 사람들을 태워주려고 한다.

오늘 상근이의 수상 택시를 타려고 하는 사람은 총 N명이다. 상근이는 각 사람들이 탑승할 위치와 목적지를 알고 있다. 상근이의 보트는 매우 커서 N명 모두 보트에 태울 수 있다.

예를 들어, 사람 A가 2번 집에서 8번으로 가려고 하고, B가 6에서 4로 가려고 하는 경우를 생각해보자. 상근이는 0번 집에서 시작해서, 2번에서 A를 태우고, 6번에서 B를 태울 것이다. 그 다음 4로 돌아가 B를 내려주고, 8번에서 A를 내려다준다. 그 다음에 원래 상근이가 가려고 했던 M번 집으로 가면 된다.

상근이가 모든 사람을 데려다주고, M번 집으로 가기 위해서 이동해야 하는 거리의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. (N ≤ 300,000, 3 ≤ M ≤ 109)

다음 N개 줄에는 각 사람이 상근이의 수상 택시를 타는 위치와 목적지가 주어진다. 모든 숫자는 0과 M 사이이다.

출력
첫째 줄에 상근이의 이동 거리의 최솟값을 출력한다.

예제 입력 1 
2 10
2 8
6 4
예제 출력 1 
14
출처
Olympiad > Croatian Highschool Competitions in Informatics > 2011 > Croatian Olympiad in Informatics 2011 3번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: jake0713, kks227
'''
from sys import stdin

readline = stdin.readline

N, M = map(int, readline().split())
arr = []

for _ in range(N):
    s, e = map(int, readline().split())
    if s > e:
        arr.append((e, s))

arr.sort()

dist = M
left, right = 0, 0

for e, s in arr:
    if e <= right:
        right = max(s, right)
    else:
        dist += 2 * (right - left)
        left = e
        right = s
else:
    dist += 2 * (right - left)

print(dist)