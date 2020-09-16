'''

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	7095	995	668	20.901%
문제
기상학에서 주요 사용하는 대표값은 중앙값이다. (중앙값의 정의는 힌트에 나와있다)

상근이는 1초에 한 번씩 온도를 재는 기계를 가지고 있고, 이 기계에 들어갈 소프트웨어를 작성하려고 한다.
기계에는 작은 디지털 디스플레이가 하나 달려있다. 매 초마다 디스플레이는 지난 K초동안 측정한 온도의 중앙값을 화면에 보여준다.

상근이는 소프트웨어를 기계에 올리기 전에 컴퓨터에서 테스트해보려고 한다.

총 N초 동안 측정한 온도가 주어졌을 때, 디스플레이에 표시된 중앙값의 합을 구하는 프로그램을 작성하시오.
즉, N개의 수가 주어졌을 때, 길이가 K인 연속 부분 수열 N-K+1개의 중앙값의 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 250,000, 1 ≤ K ≤ 5,000, K ≤ N)

둘째 줄부터 N개 줄에 측정한 온도가 순서대로 주어진다. 온도는 0보다 크거나 같고, 65535보다 작거나 같은 정수이다.

출력
길이가 K인 모든 연속 부분 수열의 중앙값의 합을 출력한다.

예제 입력 1
10 3
3
4
5
6
7
8
9
10
11
12
예제 출력 1
60

9 3
3
4
5
6
7
8
9
10
11

49

5 5
11
13
12
14
15

13

6 6
1
2
6
5
4
3

3
힌트
수 K개의 중앙값은 ((K+1)/2)번째로 작은 숫자이다. 인덱싱은 1번 부터 시작하며, K가 홀수인 경우를 처리하기 위해 1을 더한다.

예를 들어, (1, 2, 6, 5, 4, 3)의 중앙값은 3이고, (11, 13, 12, 14, 15)의 중앙값은 13이다.

출처
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: namnamseo njw1204 previc1
메모
'''

from sys import stdin
readline = stdin.readline

def medians(k,arr):
    idx = (k//2 if k%2 == 0 else (k+1)//2)-1
    total = 0
    # for i in range(k, len(arr)):

    return total

def init():
    N, K = map(int,readline().split())
    arr = [int(readline()) for _ in range(N)]
    return K, arr

def main():
    k, nums = init()
    res = medians(k,nums)
    print(res)

if __name__ == '__main__':
    main()
