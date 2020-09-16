'''
백조의 호수 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	7710	1621	874	19.298%
문제
두 마리의 백조가 호수에서 살고 있었다. 그렇지만 두 마리는 호수를 덮고 있는 빙판으로 만나지 못한다.

호수는 가로로 R, 세로로 C만큼의 직사각형 모양이다. 어떤 칸은 얼음으로 덮여있다.

호수는 차례로 녹는데, 매일 물 공간과 접촉한 모든 빙판 공간은 녹는다.
두 개의 공간이 접촉하려면 가로나 세로로 닿아 있는 것만 (대각선은 고려하지 않는다) 생각한다.

아래에는 세 가지 예가 있다.

...XXXXXX..XX.XXX ....XXXX.......XX .....XX..........
....XXXXXXXXX.XXX .....XXXX..X..... ......X..........
...XXXXXXXXXXXX.. ....XXX..XXXX.... .....X.....X.....
..XXXXX..XXXXXX.. ...XXX....XXXX... ....X......XX....
.XXXXXX..XXXXXX.. ..XXXX....XXXX... ...XX......XX....
XXXXXXX...XXXX... ..XXXX.....XX.... ....X............
..XXXXX...XXX.... ....XX.....X..... .................
....XXXXX.XXX.... .....XX....X..... .................
      처음               첫째 날             둘째 날
백조는 오직 물 공간에서 세로나 가로로만(대각선은 제외한다) 움직일 수 있다.

며칠이 지나야 백조들이 만날 수 있는 지 계산하는 프로그램을 작성한다.

입력
입력의 첫째 줄에는 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1500.

각 R줄 동안 C만큼의 문자열이 주어진다.

'.'은 물 공간, 'X'는 빙판 공간, 'L'은 백조가 있는 공간으로 나타낸다.

출력
첫째 줄에 문제에서 주어진 걸리는 날을 출력한다.

예제 입력 1
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
예제 출력 1
2
출처
Olympiad > Croatian Highschool Competitions in Informatics > 2005 > National Competition #2 - Seniors 2번

문제를 번역한 사람: baemin0103
알고리즘 분류
보기

메모
메모 작성하기
'''
from sys import stdin
from collections import deque
input = stdin.readline
offset = [(1,0),(0,1),(-1,0),(0,-1)]

# dfs
# disjoint set 이용해보기
# def isMeetSwan(swans, day):
#     start, end = swans
#     q = deque([start])
#     visited = set([start])
#     while(q):
#         i,j = q.popleft()
#
#         if (i,j) == end:
#             return True
#
#         for wi, wj in offset:
#             nxt = (i+wi, j+wj)
#             if nxt in water and water[nxt] >= day and nxt not in visited:
#                 visited.add(nxt)
#                 q.append(nxt)
#
#     return False
visited = set()
def isMeetSwan(s,e,d):
    if s == e:
        return True

    for wi, wj in offset:
        nxt = (s[0] + wi, s[1] + wj)
        if nxt in water and water[nxt] >= d and nxt not in visited:
            visited[nxt] = d
            isMeetSwan(nxt,e,d)
    return False

R,C = map(int,input().split())
water = {}
ice = set()
swans = []
count = 0

for i in range(R):
    rake = input().strip()
    for j in range(C):
        cur = (i,j)
        if rake[j] == 'X':
            ice.add(cur)
        else:
            water[cur] = 0
            if rake[j] == 'L':
                swans.append(cur)

while ice:
    count += 1
    next_ice = set()

    for i,j in ice:
        for wi,wj in offset:
            nxt = (i+wi, j+wj)
            if nxt in water and water[nxt] < count:
                water[(i,j)] = count
                break
        else:
            next_ice.add((i,j))

    ice = next_ice

left, mid, right = 0, 0, count
while left+1 != right:
    mid = (left+right)//2
    # print(left,mid,right)
    # print(visited)
    visited = set()
    # if isMeetSwan(swans, mid):
    if isMeetSwan(swans[0], swans[1], mid):
        right = mid
    else:
        left = mid

print(mid)


# from heapq import heappop, heappush
# start = swans[0]
# end = swans[1]
# hq = [(0,start)]
# # D = [[float('inf') for _ range(C)] for _ in range(R)]
# visited = set()
# while hq:
#     print(hq)
#     day, pos = heappop(hq)
#
#     if pos == end:
#         print(day)
#         break
#
#     for wi,wj in offset:
#         nxt = pos[0]+wi, pos[1]+wj
#         if nxt in water and nxt not in visited:
#             visited.add(nxt)
#             heappush(hq,(max(water[nxt],day),nxt))
