"""
r, .

Constraints

For  of the test cases, .
Output Format

Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

Sample Input 0

aba
10
Sample Output 0

7
Explanation 0
The first  letters of the infinite string are abaabaabaa. Because there are  a's, we print  on a new line.

Sample Input 1

a
1000000000000
Sample Output 1

1000000000000
Explanation 1
Because all of the first  letters of the infinite string are a, we print  on a new line.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
from collections import Counter

def repeatedString1(s, n):
    counter = Counter(s*(n//len(s))+ s[:(n%len(s))])
    return counter[s[0]]

def repeatedString(s, n):
    chr_count = s.count('a') * (n//len(s))
    mod_chr_count = s[:n%len(s)].count('a')
    # return divmod(n,len(s))
    return chr_count + mod_chr_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())
    s = 'aba'
    s = 'abcac'
    n = 10
    s = 'ceebbcb'
    n = 3
    s = 'gfcaaaecbg'
    n = 547602
    # s.count(s[0])
    len(s)
    repeatedString(s,n)
    # 164280
    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

    0,1,2,12,14,15,19,22
