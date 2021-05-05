'''
후위 표기식2 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	7809	3594	2877	46.239%
문제
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. (3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 정수이다)

출력
계산 결과를 소숫점 둘째 자리까지 출력한다.

예제 입력 1 
5
ABC*+DE/-
1
2
3
4
5
예제 출력 1 
6.20
예제 입력 2 
1
AA+A+
1
예제 출력 2 
3.00
출처
데이터를 추가한 사람: arine
빠진 조건을 찾은 사람: ljk0411jg
문제의 오타를 찾은 사람: masioka, whtjddjs0723
'''
from sys import stdin
readline = stdin.readline

N = int(readline())
arr = readline().rstrip()
nums = {chr(ord('A') + n):int(readline()) for n in range(N)}

stack = []

for a in arr:
    if a in nums:
        stack.append(nums[a])
    else:
        x = stack.pop()
        
        if a == '+':
            stack[-1] += x
        elif a == '-':
            stack[-1] -= x
        elif a == '*':
            stack[-1] *= x
        else:
            stack[-1] /= x

print(f'{stack[-1]:.2f}')   