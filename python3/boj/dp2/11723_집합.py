'''
집합
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1.5 초	4 MB (하단 참고)	17600	5000	3364	27.940%
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다.
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.

예제 입력 1
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

예제 출력 1
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
출처
문제를 만든 사람: baekjoon
빠진 조건을 찾은 사람: djm03178
메모리 제한 안내
아래 적혀있지 않은 메모리 제한은 언어 도움말에 적혀있는 기준을 따른다.

Java: 448MB
Java (OpenJDK): 448MB
Java 11: 448MB
Kotlin (JVM): 448MB
메모
메모 작성하기
'''
a

a = 2**20-1
len(bin(a))-2

from sys import stdin,stdout
input = stdin.readline
bm = 0

for _ in range(int(input())):
    arg = input().split()
    # print(bm,arg)
    if arg[0] == 'add':
        bm |= 2**int(arg[1])
    elif arg[0] == 'remove':
        bm &= ~(2**int(arg[1]))
    elif arg[0] == 'check':
        stdout.write('1\n' if bm == bm|2**int(arg[1]) else '0\n')
    elif arg[0] == 'toggle':
        bm ^= 2**int(arg[1])
    elif arg[0] == 'empty':
        bm = 0
    elif arg[0] == 'all':
        bm = 1048575
