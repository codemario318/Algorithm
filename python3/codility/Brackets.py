'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)
content_copy
" or "[U]
content_copy
" or "{U}
content_copy
" where U is a properly nested string;
S has the form "VW
content_copy
" where V and W are properly nested strings.
For example, the string "{[()()]}
content_copy
" is properly nested but "([)()]
content_copy
" is not.

Write a function:

def solution(S)
content_copy

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}
content_copy
", the function should return 1 and given S = "([)()]
content_copy
", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(
content_copy
', '{
content_copy
', '[
content_copy
', ']
content_copy
', '}
content_copy
' and/or ')
content_copy
'.
Copyright 2009–2025 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''

OPEN = {
    '(': ')', '[': ']', '{': '}'
}

CLOSE = {
    ')': '(', ']': '[', '}': '{'
}

SUCCESS = 1
FAIL = 0


def solution(S):
    stack = []

    for b in S:
        if b in OPEN:
            stack.append(b)
            continue

        if stack[-1] == CLOSE[b]:
            stack.pop()
        else:
            return FAIL

    return SUCCESS if len(stack) == 0 else FAIL