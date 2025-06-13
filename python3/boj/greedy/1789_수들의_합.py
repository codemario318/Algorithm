'''
수들의 합

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	73511	30112	25428	41.674%
문제
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

입력
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

출력
첫째 줄에 자연수 N의 최댓값을 출력한다.

예제 입력 1
200
예제 출력 1
19
출처
문제를 만든 사람: author5
데이터를 추가한 사람: kangwh0617, newton08, upple1
'''
from sys import stdin

readline = stdin.readline

if __name__ == '__main__':
    N = int(readline())

    cur = 1
    while cur <= N:
        N -= cur
        cur += 1

    print(cur - 1)
