sticker = [14, 6, 5, 11, 3, 9, 2, 10] #36
sticker = [1, 3, 2, 5, 4]	#8
def disabled_sticker(original_size,i):
    if i == 0:
        j,k = original_size-1,1
    elif i == original_size-1:
        j,k = i-1,0
    else:
        j,k = i-1,i+1

    return {j,k,i}

def find_big(index,stickers,prev_disabled=set(),before_total=0):
    total = before_total + stickers[index]
    disabled = prev_disabled | disabled_sticker(len(stickers),index)
    max_val = 0
    if len(disabled) >= len(sticker):
        return total

    for i in range(len(stickers)):
        if i in disabled:
            continue
        else:
            temp = find_big(i,stickers,disabled,total)
            if temp > max_val:
                max_val = temp

    return max_val

def solution(sticker):
    answer = []
    for i in range(len(sticker)):
        answer.append(find_big(i,sticker))
    return max(answer)

solution(sticker)
