s = ')()('
def solution(s):
    res = 0
    for x in s:
        if x == '(':
            res += 1
        elif x == ')':
            print('no')
            res -= 1

        if res < 0:
            return False
    # return res
    # if res == 0:
    #     return True
    # else:
    #     return False

solution(s)
