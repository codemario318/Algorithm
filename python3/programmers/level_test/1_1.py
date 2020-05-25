n = 10
word = {0:'수',1:'박'}
answer = ''
for i in range(n):
    answer += word[i%2]

print(answer)
