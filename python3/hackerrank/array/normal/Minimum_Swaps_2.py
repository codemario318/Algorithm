"""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

For example, given the array  we perform the following steps:

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array.

Function Description

Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.

minimumSwaps has the following parameter(s):

arr: an unordered array of integers
Input Format

The first line contains an integer, , the size of .
The second line contains  space-separated integers .

Constraints

Output Format

Return the minimum number of swaps to sort the given array.

Sample Input 0

4
4 3 1 2
Sample Output 0

3
Explanation 0

Given array
After swapping  we get
After swapping  we get
After swapping  we get
So, we need a minimum of  swaps to sort the array in ascending order.

Sample Input 1

5
2 3 4 1 5
Sample Output 1

3
Explanation 1

Given array
After swapping  we get
After swapping  we get
After swapping  we get
So, we need a minimum of  swaps to sort the array in ascending order.

Sample Input 2

7
1 3 5 2 4 6 7
Sample Output 2

3
Explanation 2

Given array
After swapping  we get
After swapping  we get
After swapping  we get
So, we need a minimum of  swaps to sort the array in ascending order.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def minimumSwaps(arr,n):
    index = {value:pos for pos, value in enumerate(arr)}
    print(index)
    print(arr)
    cnt = 0
    for i in range(n):
        if i+1 == arr[i]:
            continue
        tmp = arr[i]
        arr[index[i+1]], arr[i] = arr[i], i+1
        index[arr[index[i+1]]] = index[i+1]
        index[i+1] = i
        cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr,n)

    fptr.write(str(res) + '\n')

    fptr.close()
