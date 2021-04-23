'''
성냥개비 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	1685	597	433	37.554%
문제
성냥개비는 숫자를 나타내기에 아주 이상적인 도구이다. 보통 십진수를 성냥개비로 표현하는 방법은 다음과 같다.



성냥개비의 개수가 주어졌을 때, 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 큰 수를 찾는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개 이다. 각 테스트 케이스는 한 줄로 이루어져 있고, 성냥개비의 개수 n이 주어진다. (2 ≤ n ≤ 100)

출력
각 테스트 케이스에 대해서 입력으로 주어진 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 가장 큰 수를 출력한다. 두 숫자는 모두 양수이어야 하고, 숫자는 0으로 시작할 수 없다. 

예제 입력 1 
4
3
6
7
15
예제 출력 1 
7 7
6 111
8 711
108 7111111
출처


ICPC > Regionals > Europe > Northwestern European Regional Contest > NWERC 2008 H번

문제를 번역한 사람: baekjoon
링크
ACM-ICPC Live Archive
TJU Online Judge
HDU Online Judge
'''
from sys import stdin
readline = stdin.readline

MAX = 100
LMT = '1'*50


def max_nums(n):
    if n % 2:
        return '7' + '1'*((n-2)//2)
    else:
        return '1'*(n//2)


def min_nums(n):
    NUM_SHEET = {2: '1', 3: '7', 4: '4', 5: '2', 6: '0', 7: '8'}
    mem = [LMT, LMT, '1', '7', '4', '2', '6', '8']

    for i in range(8, n+1):
        temp = int(LMT)

        for j, w in NUM_SHEET.items():
            a = mem[i-j]

            if w == '0':
                temp = min(temp, int(a+w), int('6'+a))
            else:
                temp = min(temp, int(a+w), int(w+a))

        mem.append(str(temp))

    return mem


def main():
    n = int(readline())

    min_mem = min_nums(MAX)

    for _ in range(n):
        num = int(readline())
        min_num = min_mem[num]
        max_num = max_nums(num)
        print(min_num, max_num)


if __name__ == '__main__':
    main()
