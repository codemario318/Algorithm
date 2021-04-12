'''
빗물 출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	3012	1594	1267	54.471%
문제
2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.



비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

입력
첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)

두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.

따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

출력
2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.

빗물이 전혀 고이지 않을 경우 0을 출력하여라.

예제 입력 1 
4 4
3 0 1 4
예제 출력 1 
5
예제 입력 2 
4 8
3 1 2 3 4 1 1 2
예제 출력 2 
5
예제 입력 3 
3 5
0 0 0 2 0
예제 출력 3 
0
힌트
힌트 1:



힌트 2:



힌트 3:



출처
University > 충남대학교 > 생각하는 프로그래밍 대회  D번

문제를 만든 사람: isku
'''
from sys import stdin
readline = stdin.readline

H, W = map(int, readline().split())
blocks = map(int, readline().split())

word = [[0 for _ in range(W)] for _ in range(H)]

for y, block in enumerate(blocks):
    for x in range(block):
        word[x][y] = '*'

res = 0

for x in range(H):
    l, r = 0, W-1

    while l < W and not word[x][l]:
        l += 1

    while r > l and not word[x][r]:
        r -= 1

    if l == r:
        break

    for y in range(l+1, r):
        res += not word[x][y]

print(res)
