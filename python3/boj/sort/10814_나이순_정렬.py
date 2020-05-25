from sys import stdin
m = lambda x: (int(x[0]),x[1])

members = [m(stdin.readline().split()) for _ in range(int(stdin.readline()))]

members.sort(key=lambda x:x[0])

for age, name in members:
    print("{} {}".format(age,name))
