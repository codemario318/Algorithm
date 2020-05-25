n = 8; a=4;b=7
i = 0
while((2**i) != n):
    a = sum(divmod(a,2))
    b = sum(divmod(b,2))

    if a == b:
        return i+1
    else:
        i += 1
i
