'''
캥거루가 x 위치에서 v의 속도로 이동하는데 두마리의 캥거루를 한번에 잡을수 있는 위치가 존재하면 YES 아니면 NO 출력.
캥거루 위치: x1 < x2
캥거루 속도: v1, v2
'''

def kangaroo(x1,v1,x2,v2):
    for i in range(2343):
        if x1+v1*i == x2+v2*i:
            print('YES')
            return
        if x1+v1*i > x2+v2*i:
            print('NO')
            return
    print('NO')
    return

def kangaroo1(x1,v1,x2,v2):
    try:
        i = (x2-x1)/(v1-v2)
    except ZeroDivisionError:
        print("NO")

    if abs(int(i)) == i:
        print("YES")
    else:
        print("NO")

x1, v1, x2, v2 = map(int,input().split())

kangaroo1(x1,v1,x2,v2)
"""
x1 + v1*i = x2 + v2*i
x1-x2 + i*(v1-v2) = 0
i*(v1-v2) = x2-x1
i = (x2-x1)/(v1-v2)
"""
