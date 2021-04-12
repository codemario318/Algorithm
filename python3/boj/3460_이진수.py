'''
이진수 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	5010	3208	2835	64.859%
문제
양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 최하위 비트(least significant bit, lsb)의 위치는 0이다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. (1 ≤ T ≤ 10, 1 ≤ n ≤ 106)

출력
각 테스트 케이스에 대해서, 1의 위치를 공백으로 구분해서 줄 하나에 출력한다. 위치가 낮은 것부터 출력한다.

예제 입력 1 
1
13
예제 출력 1 
0 2 3
출처
ICPC > Regionals > Europe > Central European Regional Contest > CERC 2001 PB번

문제의 오타를 찾은 사람: 10_J
문제를 번역한 사람: baekjoon
빠진 조건을 찾은 사람: irikong
링크
ZJU Online Judge
TJU Online Judge
HDU Online Judge
'''
from sys import stdin
readline = stdin.readline


def get_binary(n):
    res = []

    while n > 0:
        n, m = divmod(n, 2)
        res.append(m)

    return res


if __name__ == '__main__':
    T = int(readline())

    for _ in range(T):
        n = int(readline())

        b_arr = get_binary(n)
        b_idx = [i for i in range(len(b_arr)) if b_arr[i]]
        b_str = ' '.join(map(str, b_idx))

        print(b_str)
