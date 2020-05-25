from sys import stdin
if __name__ == "__main__":
    x,y,w,h = map(int,stdin.readline().split())
    print(min(w-x, h-y, x, y))
