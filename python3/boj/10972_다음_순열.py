'''
다음 순열 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	16509	6998	5025	43.215%
문제
1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.

사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 1, 2
3, 2, 1
입력
첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

출력
첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

예제 입력 1 
4
1 2 3 4
예제 출력 1 
1 2 4 3
예제 입력 2 
5
5 4 3 2 1
예제 출력 2 
-1
출처
문제를 만든 사람: baekjoon
'''
from sys import stdin
readline = stdin.readline


def get_next_perm(n, arr):
    i = n-1

    while i > 0 and arr[i] < arr[i-1]:
        i -= 1

    if i < 1:
        return False

    j = n-1

    while arr[j] <= arr[i-1]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = n-1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return True


n = int(readline())
nums = list(map(int, readline().split()))

if get_next_perm(n, nums):
    print(' '.join(map(str, nums)))
else:
    print(-1)
