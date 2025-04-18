'''
문서 검색 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	32976	15058	12042	45.346%
문제
세준이는 영어로만 이루어진 어떤 문서를 검색하는 함수를 만들려고 한다. 이 함수는 어떤 단어가 총 몇 번 등장하는지 세려고 한다. 그러나, 세준이의 함수는 중복되어 세는 것은 빼고 세야 한다. 예를 들어, 문서가 abababa이고, 그리고 찾으려는 단어가 ababa라면, 세준이의 이 함수는 이 단어를 0번부터 찾을 수 있고, 2번부터도 찾을 수 있다. 그러나 동시에 셀 수는 없다.

세준이는 문서와 검색하려는 단어가 주어졌을 때, 그 단어가 최대 몇 번 중복되지 않게 등장하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 문서가 주어진다. 문서의 길이는 최대 2500이다. 둘째 줄에 검색하고 싶은 단어가 주어진다. 이 길이는 최대 50이다. 문서와 단어는 알파벳 소문자와 공백으로 이루어져 있다.

출력
첫째 줄에 중복되지 않게 최대 몇 번 등장하는지 출력한다.

예제 입력 1
ababababa
aba
예제 출력 1
2
예제 입력 2
a a a a a
a a
예제 출력 2
2
예제 입력 3
ababababa
ababa
예제 출력 3
1
예제 입력 4
aaaaaaa
aa
예제 출력 4
3
출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: chan120317, jaehoo1
문제의 오타를 찾은 사람: hist0613

abababababa
aba

3

aaaaaa
aa

3
'''
from sys import stdin

readline = stdin.readline


def compute_lps(pattern):
    m = len(pattern)
    lps = [0 for _ in range(m)]

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def search_word_count(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    lps = compute_lps(pattern)

    i, j = 0, 0
    count = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            count += 1
            i = i - j + m
            j = 0
        elif i < n and text[i] != pattern[j]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return count

if __name__ == '__main__':
    doc = readline().rstrip()
    word = readline().rstrip()
    print(search_word_count(doc, word))
