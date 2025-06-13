'''
내려가기

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	4 MB (하단 참고)	53623	20682	16195	36.752%
문제
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.



별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.

입력
첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

출력
첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

예제 입력 1
3
1 2 3
4 5 6
4 9 0
예제 출력 1
18 6
예제 입력 2
3
0 0 0
0 0 0
0 0 0
예제 출력 2
0 0

2
1 10 1
2 1 1

12 2

출처
빠진 조건을 찾은 사람: dreamian
잘못된 데이터를 찾은 사람: tncks0121
알고리즘 분류
보기

메모리 제한
Java 8: 256 MB
Java 8 (OpenJDK): 256 MB
Java 11: 256 MB
Kotlin (JVM): 256 MB
'''

from sys import stdin

readline = stdin.readline

if __name__ == '__main__':
    N = int(readline())
    prev_max = list(map(int, readline().split()))
    prev_min = prev_max[:]

    for _ in range(N - 1):
        cur_max = list(map(int, readline().split()))
        cur_min = cur_max[:]

        cur_max[0] += max(prev_max[0], prev_max[1])
        cur_max[1] += max(prev_max[0], prev_max[1], prev_max[2])
        cur_max[2] += max(prev_max[1], prev_max[2])
        prev_max = cur_max

        cur_min[0] += min(prev_min[0], prev_min[1])
        cur_min[1] += min(prev_min[0], prev_min[1], prev_min[2])
        cur_min[2] += min(prev_min[1], prev_min[2])
        prev_min = cur_min

    print(max(prev_max), min(prev_min))
