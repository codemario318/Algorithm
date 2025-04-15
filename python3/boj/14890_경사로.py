'''
경사로

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	33868	19378	14209	57.852%
문제
크기가 N×N인 지도가 있다. 지도의 각 칸에는 그 곳의 높이가 적혀져 있다.

오늘은 이 지도에서 지나갈 수 있는 길이 몇 개 있는지 알아보려고 한다. 길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것이다.

다음과 같은 N=6인 경우 지도를 살펴보자.



이때, 길은 총 2N개가 있으며, 아래와 같다.



길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다. 또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다. 경사로는 높이가 항상 1이며, 길이는 L이다. 또, 개수는 매우 많아 부족할 일이 없다. 경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.

경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
아래와 같은 경우에는 경사로를 놓을 수 없다.

경사로를 놓은 곳에 또 경사로를 놓는 경우
낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
경사로를 놓다가 범위를 벗어나는 경우
L = 2인 경우에 경사로를 놓을 수 있는 경우를 그림으로 나타내면 아래와 같다.



경사로를 놓을 수 없는 경우는 아래와 같다.



위의 그림의 가장 왼쪽부터 1번, 2번, 3번, 4번 예제라고 했을 때, 1번은 높이 차이가 1이 아니라서, 2번은 경사로를 바닥과 접하게 놓지 않아서, 3번은 겹쳐서 놓아서, 4번은 기울이게 놓아서 불가능한 경우이다.

가장 위에 주어진 그림 예의 경우에 지나갈 수 있는 길은 파란색으로, 지나갈 수 없는 길은 빨간색으로 표시되어 있으며, 아래와 같다. 경사로의 길이 L = 2이다.



지도가 주어졌을 때, 지나갈 수 있는 길의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)이 주어진다. 둘째 줄부터 N개의 줄에 지도가 주어진다. 각 칸의 높이는 10보다 작거나 같은 자연수이다.

출력
첫째 줄에 지나갈 수 있는 길의 개수를 출력한다.

예제 입력 1
6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2
예제 출력 1
3
예제 입력 2
6 2
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
예제 출력 2
7
예제 입력 3
6 3
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
예제 출력 3
3
예제 입력 4
6 1
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
예제 출력 4
11
힌트
예제 2의 경우 아래와 같은 파란색 길을 지나갈 수 있다.



예제 3의 경우에는 아래와 같은 파란색 길이 지나갈 수 있는 길이다.



마지막으로, 예제 4의 경우에는 아래와 같은 파란색 길이 지나갈 수 있는 길이다.



출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: byon26, da3107, kimyh0316, qkrjh0904
'''
from collections import deque, Counter
from sys import stdin

readline = stdin.readline


def solution(arr, window_size):
    print(arr)
    window = deque()
    counter = Counter()

    for num in arr[:window_size]:
        if not window or window[-1] == num:
            window.append(num)
            counter[num] += 1
        else:
            return False

    for cur in arr[window_size:]:
        print(window)
        print(counter)

        if cur == window[-1]:
            window.append(cur)
            counter[cur] += 1
            counter[window.popleft()] -= 1
            continue

        if cur < window[-1] or cur - window[-1] > 1:
            return False

        if counter[window[-1]] != window_size:
            return False

        counter[window.popleft()] -= 1

        window.append(cur)
        counter[cur] += 1
    print('True')
    return True


if __name__ == '__main__':
    N, L = map(int, readline().split())
    board = [list(map(int, readline().split())) for _ in range(N)]

    total_count = 0

    for i in range(N):
        row = board[i]
        total_count += solution(row, L) or solution(list(reversed(row)), L)

        col = [board[j][i] for j in range(N)]
        total_count += solution(col, L) or solution(list(reversed(col)), L)

    print(total_count)
