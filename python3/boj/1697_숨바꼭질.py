'''
숨바꼭질 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	107420	30114	18732	24.997%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
힌트
수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.

출처
Olympiad > USA Computing Olympiad > 2006-2007 Season > USACO US Open 2007 Contest > Silver 2번

문제를 번역한 사람: author6
데이터를 추가한 사람: djm03178
링크
PKU Judge Online
TJU Online Judge
비슷한 문제
12851번. 숨바꼭질 2
13549번. 숨바꼭질 3
13913번. 숨바꼭질 4
'''
MAX = 100000

n, k = map(int, input().split())
visited = [False for _ in range(MAX+1)]

visited[n] = 0

if n >= k:
    print(n-k)
else:
    q = [(n, 0)]

    while q:
        cur, time = q.pop(0)

        if cur == k:
            print(time)
            break
        else:
            if cur < MAX and not visited[cur+1]:
                visited[cur+1] = True
                q.append((cur+1, time+1))
            if cur*2 <= MAX and not visited[cur*2]:
                visited[cur*2] = True
                q.append((cur*2, time+1))
            if cur > 0 and not visited[cur-1]:
                visited[cur-1] = True
                q.append((cur-1, time+1))
