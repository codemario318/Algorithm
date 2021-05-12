'''
2진수 8진수 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	17204	6325	5123	38.825%
문제
2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

입력
첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.

예제 입력 1 
11001100
예제 출력 1 
314
출처
문제를 만든 사람: author5
데이터를 추가한 사람: sheepbomb
비슷한 문제
1212번. 8진수 2진수
'''
from collections import deque

bins = list(map(int, input().rstrip()))
octs = deque()

temp = 1 if bins[-1] else 0
n = 1

bins.pop()

while bins:
    num = bins.pop()

    if n % 3 == 0:
        octs.appendleft(temp)
        temp = 0

    if num:
        temp += 2**(n % 3)

    n += 1

if temp:
    octs.appendleft(temp)

while octs and not octs[0]:
    octs.popleft()

if octs:
    print(''.join(map(str, octs)))
else:
    print(0)