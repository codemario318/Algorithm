'''
접미사 배열

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	29239	20646	17238	71.477%
문제
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.

baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고, 이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.

문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

출력
첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.

예제 입력 1
baekjoon
예제 출력 1
aekjoon
baekjoon
ekjoon
joon
kjoon
n
on
oon
출처
문제를 만든 사람: baekjoon
'''

from sys import stdin

readline = stdin.readline

if __name__ == '__main__':
    S = stdin.readline().strip()

    for suffix in sorted([S[i: len(S)] for i in range(len(S))]):
        print(suffix)
