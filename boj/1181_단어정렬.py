from functools import cmp_to_key

def compare(x, y):
	if(len(x) < len(y)):
		return -1
	elif(len(x) > len(y)):
		return 1
	else:
		if(x < y): # x[1]과 y[1]을 비교해서 y[1]이 크면
			return -1 # x 내용을 앞으로 보냄
		elif(x > y):
			return 1
		else:
			return 0

num = int(input())
' df '.strip()
words = set()
for n in range(num):
    words.add(input())

for word in sorted(words,key=lambda x:(len(x),x)):
    print(word)
'''
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''
