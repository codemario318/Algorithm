from sys import stdin, setrecursionlimit
import math

read = lambda: map(int, stdin.readline().split())

def tree_init(node, start, end):
    global tree, costs
    if start == end:
        tree[node] = costs[start]
        return tree[node]
    else:
        left = tree_init(node*2, start,(start+end)//2)
        right = tree_init(node*2+1,(start+end)//2+1, end)
        tree[node] = left + right
        return tree[node]

def get_sum(node, start, end, left, right):
    global tree
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return get_sum(node*2, start, (start+end)//2, left, right) + get_sum(node*2+1, (start+end)//2+1, end, left, right)

if __name__ == '__main__':
    global tree, costs
    N,M = read()
    costs = list(read())

    tree_height = math.ceil(math.log2(N))+1
    tree = [0 for _ in range(2**tree_height)]
    tree_init(1, 0, N-1)
    print(tree)
    for _ in range(M):
        start, end = read()
        print(get_sum(1,1, N, start, end))
