'''
백설 공주와 일곱 난쟁이 스페셜 저지출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	4721	3164	2774	70.086%
문제
매일 매일 일곱 난쟁이는 광산으로 일을 하러 간다. 난쟁이가 일을 하는 동안 백설공주는 그들을 위해 저녁 식사를 준비한다. 백설공주는 의자 일곱개, 접시 일곱개, 나이프 일곱개를 준비한다.

어느 날 광산에서 아홉 난쟁이가 돌아왔다. (왜 그리고 어떻게 아홉 난쟁이가 돌아왔는지는 아무도 모른다) 아홉 난쟁이는 각각 자신이 백설공주의 일곱 난쟁이라고 우기고 있다.

백설공주는 이런 일이 생길 것을 대비해서, 난쟁이가 쓰고 다니는 모자에 100보다 작은 양의 정수를 적어 놓았다. 사실 백설 공주는 공주가 되기 전에 매우 유명한 수학자였다. 따라서, 일곱 난쟁이의 모자에 쓰여 있는 숫자의 합이 100이 되도록 적어 놓았다.

아홉 난쟁이의 모자에 쓰여 있는 수가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램을 작성하시오. (아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾으시오)

입력
총 아홉개 줄에 1보다 크거나 같고 99보다 작거나 같은 자연수가 주어진다. 모든 숫자는 서로 다르다. 또, 항상 답이 유일한 경우만 입력으로 주어진다.

출력
일곱 난쟁이가 쓴 모자에 쓰여 있는 수를 한 줄에 하나씩 출력한다.

예제 입력 1 
7
8
10
13
15
19
20
23
25
예제 출력 1 
7
8
10
13
19
20
23
출처
Contest > Croatian Open Competition in Informatics > COCI 2006/2007 > Contest #3 1번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: bvba
링크
TJU Online Judge

'''

from sys import stdin
from itertools import combinations
TOTAL = 9
REAL = 7

def readline():
    return int(stdin.readline())

def solution(arr):
    for comb in combinations(arr, REAL):
        cand = list(comb)
        if sum(cand) == 100:
            return '\n'.join(map(str, cand))

if __name__ == "__main__":
    dwarfs = [readline() for _ in range(TOTAL)]
    dwarfs.sort()
    print(solution(dwarfs))

    


