'''
1, 2, 3 더하기 4 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	2116	1371	1050	66.540%
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.

1+1+1+1
2+1+1 (1+1+2, 1+2+1)
2+2
1+3 (3+1)
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 10,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

예제 입력 1 
3
4
7
10
예제 출력 1 
4
8
14
출처
문제를 만든 사람: baekjoon
'''
from sys import stdin
readline = stdin.readline
MAX = 10000


def solution():
    mem = [[0, 0, 0] for _ in range(MAX+1)]

    mem[1][0] = 1
    mem[2][0] = 1
    mem[2][1] = 1
    mem[3][0] = 1
    mem[3][1] = 1
    mem[3][2] = 1

    for i in range(4, MAX+1):
        mem[i][0] = 1
        mem[i][1] = mem[i-2][0] + mem[i-2][1]
        mem[i][2] = mem[i-3][0] + mem[i-3][1] + mem[i-3][2]

    return mem


def main():
    n = int(readline())
    mem = solution()

    for _ in range(n):
        num = int(readline())
        print(sum(mem[num]))


if __name__ == '__main__':
    main()
