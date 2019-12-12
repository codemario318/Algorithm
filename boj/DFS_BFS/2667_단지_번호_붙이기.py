'''
단지번호붙이기
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	40616	15764	10389	38.079%

문제
<그림 1>과 같이 정사각형 모양의 지도가 있다.
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.

철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.

대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고,
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오.
 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

5
00000
00000
00000
00000
00000

5
10101
01010
10101
01010
10101

예제 출력 1
3
7
8
9
출처
Olympiad > 한국정보올림피아드 > KOI 1996 > 초등부 1번

잘못된 데이터를 찾은 사람: djm03178
데이터를 추가한 사람: djm03178 jh05013
문제의 오타를 찾은 사람: metadata
알고리즘 분류
보기

메모
'''

from sys import stdin
input = stdin.readline

N = int(input())
homes = [list(map(int,list(input().rstrip()))) for _ in range(N)]

x,y  = 0,0
count = 0
next = []
answer = []

while True:
    if x >= N or y >= N:
        break
    if homes[x][y] == 1:
        homes[x][y] = 0
        next.append((x,y))
        count += 1

        while next:
            nx, ny = next.pop()
            for xw,yw in ((0,1),(1,0),(-1,0),(0,-1)):
                if 0 <= nx+xw < N and 0 <= ny+yw < N:
                    if homes[nx+xw][ny+yw]:
                        next.append((nx+xw,ny+yw))
                        homes[nx+xw][ny+yw] = 0
                        count += 1
        answer.append(count)
        count = 0
    else:
        if y < N-1:
            y += 1
        else:
            y = 0
            x += 1
print(len(answer))
for a in sorted(answer):
    print(a)
