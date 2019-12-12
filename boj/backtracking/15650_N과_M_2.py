'''
N과 M (2)

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	3656	2870	2148	78.855%

문제

자연수 N과 M이 주어졌을 때,
아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1

3 1

예제 출력 1
1
2
3

예제 입력 2

4 2

예제 출력 2
1 2
1 3
1 4
2 3
2 4
3 4

예제 입력 3

4 4

예제 출력 3
1 2 3 4

출처
문제를 만든 사람: baekjoon
메모
메모 작성하기
'''
def solution(nums, visited):
    if len(nums) == M:
        print(' '.join(map(str,nums)))
    else:
        for i in range(nums[-1] if nums else 0,N):
            if visited[i] == False:
                temp = visited.copy()
                temp[i] = True
                solution(nums+[i+1],temp)

N,M = map(int,input().split())
solution([],[False for _ in range(N)])
