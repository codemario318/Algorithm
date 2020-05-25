'''
4
1 1
2 4
3 2
4 3

1

5
3 4
1 5
4 2
2 3
5 1

'''


from sys import stdin

if __name__ == "__main__":
    N = int(stdin.readline())
    wires = [list(map(int,stdin.readline().split())) for _ in range(N)]
    mem = [0 for _ in range(N)]

    wires.sort()
    mem[0] = 1

    for i in range(1,N):
        temp = 1
        for j in range(i):
            if wires[i][1] > wires[j][1]:
                temp = max(temp,mem[j]+1)
        mem[i] = temp

    print(N-max(mem))
