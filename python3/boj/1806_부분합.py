'''
부분합 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (하단 참고)	128 MB	26955	6937	4931	25.614%
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

예제 입력 1 
10 15
5 1 3 5 10 7 4 9 2 8
예제 출력 1 
2

3 100
1 1 1

0

10 21
11 2 5 6 8 9 2 3 10 9 10


5 5
1 1 1 1 1

5

10 10
1 1 1 1 1 1 1 1 1 10

1
출처
ICPC > Regionals > Europe > Southeastern European Regional Contest > SEERC 2006 B번

문제를 번역한 사람: author5
시간 제한을 수정한 사람: cheetose
잘못된 조건을 찾은 사람: isku
데이터를 추가한 사람: ppqhdl2, wookje, YunGoon
빠진 조건을 찾은 사람: rlarlghks970113
문제의 오타를 찾은 사람: ZZangZZang
링크
ACM-ICPC Live Archive
PKU Judge Online
ZJU Online Judge
TJU Online Judge

'''
from sys import stdin
def readline(): return map(int, stdin.readline().split())


N, S = readline()
arr = list(readline())

min_len = float('inf')

s, e = 0, 0
total = 0
cur_len = 0

while s < N and e < N:
    if total < S:
        total += arr[e]
        cur_len += 1
        e += 1
    else:
        min_len = min(min_len, cur_len)
        total -= arr[s]
        cur_len -= 1
        s += 1

while total >= S and s < N:
    min_len = min(min_len, cur_len)
    total -= arr[s]
    cur_len -= 1
    s += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)
