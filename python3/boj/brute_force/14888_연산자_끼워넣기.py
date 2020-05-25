from sys import stdin

add = lambda x,y: x+y
sub = lambda x,y: x-y
sqr = lambda x,y: x*y
div = lambda x,y: int(x/y)

OPERATORS = (add, sub, sqr, div)

def sol(idx,res):
    if N == idx:
        answer.append(res)
    else:
        for i in range(4):
            if opers[i] > 0:
                opers[i] -= 1
                sol(idx+1,OPERATORS[i](res,nums[idx]))
                opers[i] += 1

if __name__ == '__main__':
    N = int(stdin.readline())
    answer = []
    nums = list(map(int, stdin.readline().split()))
    opers = list(map(int,stdin.readline().split()))

    sol(1,nums[0])

    print(max(answer))
    print(min(answer))
