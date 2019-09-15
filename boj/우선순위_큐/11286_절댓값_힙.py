'''
절댓값 힙
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초 (언어별 추가 시간 없음)	256 MB	4058	1870	1479	51.141%
문제
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력
첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.

출력
입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

예제 입력 1
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
예제 출력 1
-1
1
0
-1
-1
1
1
-2
2
0
출처
문제를 만든 사람: baekjoon
잘못된 조건을 찾은 사람: dkim
데이터를 추가한 사람: nova9128
문제의 오타를 찾은 사람: sgchoi5 youngminz zerozero
비슷한 문제
1927번. 최소 힙
11279번. 최대 힙
알고리즘 분류
'''

from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

N = int(input())
heap = []

for _ in range(N):
    n = int(input())
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap,(abs(n),n))
