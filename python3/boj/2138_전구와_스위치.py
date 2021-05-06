'''
전구와 스위치 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	2956	1105	877	38.703%
문제
N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는(1) 상태와 꺼져 있는 (0) 상태 중 하나의 상태를 가진다. i(1<i<N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(2≤N≤100,000)이 주어진다. 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다.

출력
첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.

예제 입력 1 
3
000
010
예제 출력 1 
3
알고리즘 분류
보기
'''
from sys import stdin
readline = stdin.readline


def toggle(val):
    return '1' if val == '0' else '0'


def turn(arrA, arrB):
    count = 0

    for i in range(1, N-1):
        if arrA[i-1] != arrB[i-1]:
            count += 1
            arrA[i-1] = toggle(arrA[i-1])
            arrA[i] = toggle(arrA[i])
            arrA[i+1] = toggle(arrA[i+1])

    if arrA[-2] != arrB[-2]:
        count += 1
        arrA[-1] = toggle(arrA[-1])
        arrA[-2] = toggle(arrA[-2])

    if arrA == arrB:
        return count
    else:
        return float('inf')


N = int(readline())

A = list(readline().rstrip())
B = list(readline().rstrip())

changeA = A[:]

changeA[0] = toggle(changeA[0])
changeA[1] = toggle(changeA[1])

count = turn(A, B)
changeCount = turn(changeA, B) + 1

res = min(count, changeCount)

if res == float('inf'):
    print(-1)
else:
    print(res)
