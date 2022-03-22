from collections import deque

CONVERT_NUMBER = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}


def solution(s):
    numbers = []
    word = ''

    for char in s:
        word += char

        if word not in CONVERT_NUMBER:
            continue

        number = CONVERT_NUMBER[word]
        numbers.append(number)

        word = ''

    result = int(''.join(numbers))

    return result