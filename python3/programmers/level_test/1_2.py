answers = [1,2,3,4,5]
supo_1 = '12345'*(len(answers)//5) + '12345'[:len(answers)%5]
supo_2 = '21232425'*(len(answers)//8) + '21232425'[:len(answers)%8]
supo_3 = '3311224455'*(len(answers)//10) + '3311224455'[:len(answers)%10]

answer = {1:0,2:0,3:0}

for i,sol in enumerate(answers):
    if int(supo_1[i]) == sol:
        answer[1] += 1
    if int(supo_2[i]) == sol:
        answer[2] += 1
    if int(supo_3[i]) == sol:
        answer[3] += 1

res = []
max_val = 0
for k,v in sorted(answer.items(),key=lambda x: answer[x[0]],reverse=True):
    if len(res) == 0:
        res.append(k)
        max_val = v
    elif v == max_val:
        res.append(k)
    else:
        break
return res
