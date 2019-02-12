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

words = {}
for n in range(num):
    word = input()
    try:
        words[word] += 1
    except KeyError:
        words[word] = 1

for word in sorted(words.keys(),key=cmp_to_key(compare)):
    print(word)
