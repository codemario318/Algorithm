'''
제한사항
s의 길이는 1 이상 1,000 이하입니다.
s는 알파벳 소문자로만 이루어져 있습니다.
입출력 예
s	result
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17
입출력 예에 대한 설명
입출력 예 #1

문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.

입출력 예 #2

문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.

입출력 예 #3

문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.

입출력 예 #4

문자열을 2개 단위로 자르면 abcabcabcabc6de 가 됩니다.
문자열을 3개 단위로 자르면 4abcdededededede 가 됩니다.
문자열을 4개 단위로 자르면 abcabcabcabc3dede 가 됩니다.
문자열을 6개 단위로 자를 경우 2abcabc2dedede가 되며, 이때의 길이가 14로 가장 짧습니다.

입출력 예 #5

문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.
이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.
'''

def solution(s):
    answer = []
    split_s = [[s[j:j+i] for j in range(0,len(s),i)] for i in range(1,len(s))]

    for words in split_s:
        count = 1
        w = words[0]
        temp = []
        for i in range(1,len(words)):
            if words[i] == w:
                count += 1
            else:
                temp.append(str(count)+w if count > 1 else w)
                count = 1
                w = words[i]
        answer.append(len(''.join(temp)+(str(count) if count >1 else '')+w))
    return min(answer) if answer else s
# import re
# re.findall('[a]{3,3}',"aabbaccc")
# def solution(s):
#     answer = 0
#     split_s = [[s[j:j+i] for j in range(0,len(s),i)] for i in range(1,len(s))]
#     split_s
#     for words in split_s:
#         temp = ''
#         count = 1
#         for i in range(1,len(words)):
#
#
#     return answer


solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")
solution("x")
