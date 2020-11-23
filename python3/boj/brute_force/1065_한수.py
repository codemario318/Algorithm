'''
한수 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	57079	29051	24856	51.225%
문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

예제 입력 1 
110
예제 출력 1 
99
예제 입력 2 
1
예제 출력 2 
1
예제 입력 3 
210
예제 출력 3 
105
예제 입력 4 
1000
예제 출력 4 
144
출처
문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: bdh3313
잘못된 데이터를 찾은 사람: djm03178
데이터를 추가한 사람: jh05013
'''


def getNumCount(num, lmt, term):
    last = int(num[-1]) + term
    nextNum = num + str(last)

    if 0 <= last < 10 and int(nextNum) <= lmt:   
        return 1 + getNumCount(nextNum, lmt, term)
    return  0


if __name__ == "__main__":
    n = int(input())
    count = 0

    for base in range(1, 10):
        if base <= n:
            count += 1
        for term in range(-9, 10, 1):
            count += getNumCount(str(base), n, term)

    print(count)
