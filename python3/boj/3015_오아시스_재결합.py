'''
오아시스 재결합 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	32009	8756	6658	27.656%
문제
오아시스의 재결합 공연에 N명이 한 줄로 서서 기다리고 있다.

이 역사적인 순간을 맞이하기 위해 줄에서 기다리고 있던 백준이는 갑자기 자기가 볼 수 있는 사람의 수가 궁금해졌다.

두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.

줄에 서 있는 사람의 키가 주어졌을 때, 서로 볼 수 있는 쌍의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 줄에서 기다리고 있는 사람의 수 N이 주어진다. (1 ≤ N ≤ 500,000)

둘째 줄부터 N개의 줄에는 각 사람의 키가 나노미터 단위로 주어진다. 모든 사람의 키는 231 나노미터 보다 작다.

사람들이 서 있는 순서대로 입력이 주어진다.

출력
서로 볼 수 있는 쌍의 수를 출력한다.

예제 입력 1
7
2
4
1
2
2
5
1
예제 출력 1
10
출처
Olympiad > Croatian Highschool Competitions in Informatics > 2007 > Croatian Olympiad in Informatics 2007 1번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: kiwiyou
'''

from sys import stdin

readline = stdin.readline


def solution(heights):
    stack = []
    pair_count = 0

    for height in heights:
        same_height_count = 1

        while stack and stack[-1][0] <= height:
            prev_height, prev_count = stack.pop()

            if prev_height == height:
                pair_count += prev_count
                same_height_count += prev_count
            else:
                pair_count += prev_count

        if stack:
            pair_count += 1

        stack.append((height, same_height_count))

    return pair_count


if __name__ == '__main__':
    N = int(readline())
    heights = [int(readline()) for _ in range(N)]
    print(solution(heights))
