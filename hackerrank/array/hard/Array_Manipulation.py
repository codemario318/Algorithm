"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros . Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Constraints

Output Format

Return the integer maximum value in the finished array.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update list will be 100 100 0 0 0.
After the second update list will be 100 200 100 100 100.
After the third update list will be 100 200 200 200 100.
The required answer will be .
"""
"""
처음 n개 0을 원소를 가지는 리스트로 시작해서
a~b 번째 까지의 원소에 k를 더한다.
마지막으로 최대 값을 출력한다.
"""
#!/bin/python3
test_8 = open('hackerrank/array/hard/Array_Manipulation_input08.txt','r')
queries = []
queries
for query in test_8.read().split('\n'):
    queries.append(list(map(int, query.rstrip().split())))
n = 1000000
len(queries)
[0] * n
n = 10
queries = queries[1:]
# len(queries)
queries = [[2, 6, 8],
            [3, 5, 7],
            [1, 8, 1],
            [5, 9, 15]]
queries = [[1, 2, 100],
            [2 ,5 ,100],
            [3 ,4, 100]]
arrayManipulation(n,queries)
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    index = {}
    max_val = 0
    for a,b,k in queries:
        for i in range(a-1,b):
            print(a)
            try:
                index[i] += k
            except KeyError:
                index[i] = k
            if max_val < index[i]:
                max_val = i

    return index
#### DIFF를 이용한 풀이
def arrayManipulation(n, queries):
    arr = [0]*(n+2)
    for a, b, k in queries:
        arr[a]+=k
        arr[b+1]-=k
    result = acc = 0
    for x in arr:
        acc+=x
        result = max(result, acc)
    return result
######
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
