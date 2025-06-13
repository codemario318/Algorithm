'''
선분 교차 2

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.25 초 (추가 시간 없음)	512 MB	26044	7065	5126	25.528%
문제
2차원 좌표 평면 위의 두 선분 L1, L2가 주어졌을 때, 두 선분이 교차하는지 아닌지 구해보자. 한 선분의 끝 점이 다른 선분이나 끝 점 위에 있는 것도 교차하는 것이다.

L1의 양 끝 점은 (x1, y1), (x2, y2), L2의 양 끝 점은 (x3, y3), (x4, y4)이다.

입력
첫째 줄에 L1의 양 끝 점 x1, y1, x2, y2가, 둘째 줄에 L2의 양 끝 점 x3, y3, x4, y4가 주어진다.

출력
L1과 L2가 교차하면 1, 아니면 0을 출력한다.

제한
-1,000,000 ≤ x1, y1, x2, y2, x3, y3, x4, y4 ≤ 1,000,000
x1, y1, x2, y2, x3, y3, x4, y4는 정수
선분의 길이는 0보다 크다.
예제 입력 1
1 1 5 5
1 5 5 1
예제 출력 1
1
예제 입력 2
1 1 5 5
6 10 10 6
예제 출력 2
0
예제 입력 3
1 1 5 5
5 5 1 1
예제 출력 3
1
예제 입력 4
1 1 5 5
3 3 5 5
예제 출력 4
1
예제 입력 5
1 1 5 5
3 3 1 3
예제 출력 5
1
예제 입력 6
1 1 5 5
5 5 9 9
예제 출력 6
1
예제 입력 7
1 1 5 5
6 6 9 9
예제 출력 7
0
예제 입력 8
1 1 5 5
5 5 1 5
예제 출력 8
1
예제 입력 9
1 1 5 5
6 6 1 5
예제 출력 9
0
출처
데이터를 추가한 사람: kkg0510, yhkee0404, wapas, tlsdydaud1, seonh4996, robo_tronic, lycoris1600, lighter, kongum, aza1200, jms020820, jmkk27, jhk2721, hunojung, dhtlq777, dbtmddn41, dankimh, cirno4143
문제의 오타를 찾은 사람: YunGoon
문제를 만든 사람: baekjoon
'''

from sys import stdin

readline = stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def solution(line_a, line_b):
    x1, y1, x2, y2 = line_a
    x3, y3, x4, y4 = line_b

    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
        if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2) or \
                max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
            return False
        return True

    return ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0


if __name__ == '__main__':
    line_a = map(int, readline().split())
    line_b = map(int, readline().split())
    print(int(solution(line_a, line_b)))
