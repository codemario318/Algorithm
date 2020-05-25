'''
문제 설명
앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

예를들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.

제한사항
문자열 s의 길이 : 2,500 이하의 자연수
문자열 s는 알파벳 소문자로만 구성
입출력 예
s	answer
abcdcba	7
abacde	3
입출력 예 설명
입출력 예 #1
4번째자리 'd'를 기준으로 문자열 s 전체가 팰린드롬이 되므로 7을 return합니다.

입출력 예 #2
2번째자리 'b'를 기준으로 aba가 팰린드롬이 되므로 3을 return합니다.
'''
s = 'abcdcba'
'12345'[::-1]
# def solution(s):
#     s[:]
#     return answer
#
# solution(s)

# '3'.upper()
# a = [[5,6],[7,8],[9,10]]
# b = [[1,2],[3,4]]
#
# def solution(arr1,arr2):
#     answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
#     for i in range(len(answer)):
#         for j in range(len(answer[0])):
#             for k in range(len(answer[0])):
#                 answer[i][j] += arr1[i][k]*arr2[k][j]
#     return answer
#
# solution(a,b)
# solution([[1, 4], [3, 2], [4, 1]],	[[3, 3], [3, 3]])
#
# def solution(s):
#     answer = []
#     for word in s.split():
#         w = list(word.lower())
#         w[0] = w[0].upper()
#         answer.append(''.join(w))
#     return ' '.join(answer)
# list(''.lower())
# solution("1 1 1")
# solution("a a a a")
# solution("Jaden  case")
# "Jaden  case".split(' ')
# '   '.split(' ')
# list('')
# from collections import Counter
# def solution(arr):
#     answer = 1
#     factors = {}
#
#     for n in arr:
#         factor = Counter()
#         i = 2
#         while n > 1:
#             d,m = divmod(n,i)
#             if m == 0:
#                 factor[i] += 1
#                 n = d
#                 i = 2
#             else:
#                 i += 1
#         for f in factor:
#             try:
#                 if factors[f] < factor[f]:
#                     factors[f] = factor[f]
#             except KeyError:
#                 factors[f] = factor[f]
#
#     for f in factors:
#         answer *= f**factors[f]
#
#     return answer

from math import gcd

def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = n * answer // gcd(n, answer)
    return answer


solution([2,6,8,14])
solution([8])
solution([3])

(2**3)*(3)*7
gcd()
'' == False
rex = re.compile('|'.join(['['+chr(c)+']{2}' for c in range(ord('a'),ord('z')+1)]))
rex.sub('','aassddccc')
import re

def solution(s):
    rex = re.compile('|'.join(['['+chr(c)+']{2}' for c in range(ord('a'),ord('z')+1)]))
    answer = '1'

    while len(s) != len(answer):
        s = rex.sub('',s)
        answer = rex.sub('',s)

    return 0 if len(answer) else 1
solution('aabb')
solution('aaebbc')
solution('aassddccc')

def solution(s):
    while True:
        temp = ['*']
        for i in range(len(s)):
            if temp[-1] == s[i]:
                temp.pop()
            else:
                temp.append(s[i])
        if len(s) == len(temp)-1:
            break
        else:
            s = temp[1:]
    return 0 if len(temp)-1 else 1

solution('aabb')
solution('aaebbc')
solution('aassddccc')
