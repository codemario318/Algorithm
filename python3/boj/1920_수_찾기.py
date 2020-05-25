'''
5
4 1 5 2 3
5
1 3 7 9 5

1
1
0
0
1
'''

from sys import stdin
from collections import Counter

if __name__ == '__main__':
    _ = stdin.readline()
    nums = Counter(stdin.readline().split())
    _ = stdin.readline()

    for n in stdin.readline().split():
        print(1 if nums[n] else 0)
