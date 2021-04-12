'''
N번째 큰 수 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	32 MB	3357	2727	2480	82.174%
문제
배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.

배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 <= T <= 1,000)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 배열 A의 원소 10개가 공백으로 구분되어 주어진다. 이 원소는 1보다 크거나 같고, 1,000보다 작거나 같은 자연수이다.

출력
각 테스트 케이스에 대해 한 줄에 하나씩 배열 A에서 3번째 큰 값을 출력한다.

예제 입력 1 
4
1 2 3 4 5 6 7 8 9 1000
338 304 619 95 343 496 489 116 98 127
931 240 986 894 826 640 965 833 136 138
940 955 364 188 133 254 501 122 768 408
예제 출력 1 
8
489
931
768
출처
ICPC > Regionals > North America > Greater New York Region > 2009 Greater New York Programming Contest A번

문제를 번역한 사람: baekjoon
잘못된 데이터를 찾은 사람: occidere
링크
ACM-ICPC Live Archive
PKU Judge Online
HDU Online Judge
'''
from sys import stdin

readline = stdin.readline
N = 3

if __name__ == '__main__':
    t = int(readline())

    for _ in range(t):
        nums = list(map(int, readline().split()))
        nums.sort()
        print(nums[-N])
