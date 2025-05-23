'''
히스토그램에서 가장 큰 직사각형 실패출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	26438	6600	4231	25.408%
문제
히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.



히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

입력
입력은 테스트 케이스 여러 개로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000) 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다. 이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다. 모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.

예제 입력 1
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
5 9 8 7 6 5
5 5 6 7 8 9
5 0 0 0 1 0
5 1 0 0 0 1
14 3 2 1 3 2 1 1 0 2 1 1 0 1 2
0
예제 출력 1
8
8
4000
25
25
1
1


3 2 1 2
1 0
2 0 0
3 0 0 0
0


출처
Contest > University of Ulm Local Contest > University of Ulm Local Contest 2003 H번

문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: eric00513
데이터를 추가한 사람: kth004, Lawali
링크
PKU Judge Online
ZJU Online Judge
TJU Online Judge
Sphere Online Judge
HDU Online Judge
'''
from sys import stdin

readline = stdin.readline


def solution(heights):
    stack = []
    max_area = 0
    i = 0

    while i < len(heights):
        if not stack or heights[stack[-1]] <= heights[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, width * heights[top])

    while stack:
        top = stack.pop()
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, width * heights[top])

    return max_area


if __name__ == '__main__':
    while True:
        N, *heights = map(int, readline().split())

        if not N:
            break

        print(solution(heights))
