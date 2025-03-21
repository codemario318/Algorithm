'''
문제 설명
정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

examples.png

제한사항
n은 1 이상 1,000 이하입니다.
입출력 예
n	result
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.
입출력 예 #2

문제 예시와 같습니다.
입출력 예 #3

문제 예시와 같습니다.
'''

from collections import deque
from itertools import chain

OFFSET = deque([(1, 0), (0, 1), (-1, -1)])


def solution(n):
    answer = [[0 for _ in range(i)] for i in range(1, n + 1)]

    target = (n * (n + 1)) // 2
    num = 1
    i, j = -1, 0

    while num <= target:
        wi, wj = OFFSET[0]
        ni, nj = i + wi, j + wj

        if 0 <= ni < n and 0 <= nj <= ni and answer[ni][nj] == 0:
            i, j = ni, nj
            answer[i][j] = num
            num += 1
        else:
            OFFSET.rotate(-1)

    return [*chain(*answer)]
