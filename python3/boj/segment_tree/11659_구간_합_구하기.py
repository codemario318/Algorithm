'''
구간 합 구하기 4
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	10319	5288	4058	51.846%
문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N (1 ≤ N ≤ 100,000), 합을 구해야 하는 횟수 M (1 ≤ M ≤ 100,000)이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

예제 입력 1
5 3
5 4 3 2 1
1 3
2 4
5 5
예제 출력 1
12
9
1
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: djm03178
메모
메모 작성하기
'''

from sys import stdin
readline = stdin.readline

class SegmentTree:
    def __init__(self, nums, start=0, end=0):
        self.valss = nums

class Node:
    def __init__(self, val, left,right):
        self.val = val
        self.left = left
        self.right = right

def init(M):
    nums = list(map(int,readline().split()))

    return

def main():
    N, M = map(int, readline().split())
    init(N)


if __name__ == '__main__':
    main()
