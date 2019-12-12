import re

def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result
n = int(input())
res = re.split('[^0+]',str(factorial(n)))[-1]
print(0 if  res==[''] else len(res))
print(n//5 + n//25 + n//125)
factorial(5)
factorial(9)
factorial(10)
factorial(15)
