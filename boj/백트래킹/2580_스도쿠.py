'''
스도쿠 스페셜 저지

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	14770	4531	2810	32.096%

문제

스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로
현재 많은 인기를 누리고 있다.

이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총
81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데,
게임 시작 전 몇 몇 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.



나머지 빈 칸을 채우는 방식은 다음과 같다.

각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.

위의 예의 경우,
첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로
첫째 줄 빈칸에는 1이 들어가야 한다.



또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이
이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.



이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.



게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때
모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

입력

아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가
한 칸씩 띄워서 차례로 주어진다.

스도쿠 판의 빈 칸의 경우에는 0이 주어진다.

스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

출력
모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉줄에 걸쳐 한 줄에
9개씩 한 칸씩 띄워서 출력한다.

스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

예제 입력 1

0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

예제 출력 1

1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1

1 3 5 4 6 9 2 7 8
7 0 0 1 3 5 6 4 9
4 0 0 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1

1 3 5 4 6 9 2 7 8
7 0 0 1 3 5 6 4 9
4 0 0 2 7 8 1 3 5
3 0 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
출처
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > 초등부 5번

Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > 중등부 3번

데이터를 추가한 사람: doju
알고리즘 분류
보기

메모
'''

# from sys import stdin
# from collections import Counter
#
# S = {0:(0,3),1:(3,6),2:(6,9)}
#
# def horizontal(_,j):
#     h = Counter([board[i][j] for i in range(9)])
#     if h[0] > 1:
#         return 0
#
#     for i in range(1,10):
#         if not h[i]:
#             return i
#
# def vertical(i,_):
#     v = Counter(board[i])
#     if v[0] > 1:
#         return 0
#
#     for i in range(1,10):
#         if not v[i]:
#             return i
#
# def square(i,j):
#     s = Counter([])
#     for a in [b[S[j//3][0]:S[j//3][1]] for b in board[S[i//3][0]:S[i//3][1]]]:
#         s.update(a)
#
#     if s[0] > 1:
#         return 0
#
#     for i in range(1,10):
#         if not s[i]:
#             return i
#
# board = [list(map(int,stdin.readline().split())) for _ in range(9)]
# emptys = [ (i,j) for i in range(9) for j in range(9) if board[i][j] == 0]
#
# while emptys:
#     e = emptys.pop(0)
#
#     for func in (vertical,horizontal,square):
#         r = func(*e)
#         if r:
#             board[e[0]][e[1]] = r
#             break
#     if not board[e[0]][e[1]]:
#         emptys.append(e)
#
# for b in board:
#     print(' '.join(map(str,b)))
# # print(board)



from sys import stdin
from collections import Counter
from copy import deepcopy
S = {0:(0,3),1:(3,6),2:(6,9)}

def horizontal(_,j):
    h = Counter([board[i][j] for i in range(9)])
    temp = []
    for i in range(1,10):
        if not h[i]:
            temp.append(i)
        elif h[i] > 1:
            return [-1]
    return temp

def vertical(i,_):
    v = Counter(board[i])
    temp = []

    for i in range(1,10):
        if not v[i]:
            temp.append(i)
        elif v[i] > 1:
            return []
    return temp

def square(i,j):
    s = Counter([])
    for a in [b[S[j//3][0]:S[j//3][1]] for b in board[S[i//3][0]:S[i//3][1]]]:
        s.update(a)

    temp = []

    for i in range(1,10):
        if not s[i]:
            temp.append(i)
        elif h[i] > 1:
            return []
    return temp

def solution(board,emptys):
    while emptys:
        e = emptys.pop(0)
        r = Counter([])

        for func in (vertical,horizontal,square):
            r.update(func(*e))

        if not r[-1]:
            return 0

        cand = [k for k,n in r.items() if n == 3]

        if len(cand) == 1:
            board[e[0]][e[1]] = cand[0]
        else:
            for c in cand:


    return

board = [list(map(int,stdin.readline().split())) for _ in range(9)]
emptys = [ (i,j) for i in range(9) for j in range(9) if board[i][j] == 0]

solution(board,emptys)


for b in board:
    print(' '.join(map(str,b)))
