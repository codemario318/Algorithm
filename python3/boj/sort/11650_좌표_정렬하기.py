from sys import stdin
inp = stdin.readline

locs = []
N = int(inp())

for _ in range(N):
    locs.append(tuple(map(int,inp().split())))

locs.sort()
for loc in locs:
    print("{} {}".format(*loc))
