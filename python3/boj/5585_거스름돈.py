if __name__ == '__main__':
    n = 1000 - int(input())
    cnt = 0
    for w in (500,100,50,10,5,1):
        if n == 0: break
        cnt += n//w
        n %= w

    print(cnt)
