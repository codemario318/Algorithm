'''
2048 (Easy) 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	35316	9045	5108	23.527%
문제
2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 링크를 누르면 게임을 해볼 수 있다.

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다.
이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
(실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)


<그림 1>	<그림 2>	<그림 3>
<그림 1>의 경우에서 위로 블록을 이동시키면 <그림 2>의 상태가 된다.
여기서, 왼쪽으로 블록을 이동시키면 <그림 3>의 상태가 된다.


<그림 4>	<그림 5>	<그림 6>	<그림 7>
<그림 4>의 상태에서 블록을 오른쪽으로 이동시키면 <그림 5>가 되고,
여기서 다시 위로 블록을 이동시키면 <그림 6>이 된다.
여기서 오른쪽으로 블록을 이동시켜 <그림 7>을 만들 수 있다.


<그림 8>	<그림 9>
<그림 8>의 상태에서 왼쪽으로 블록을 옮기면 어떻게 될까? 2가 충돌하기 때문에, 4로 합쳐지게 되고 <그림 9>의 상태가 된다.


<그림 10>	<그림 11>	<그림 12>	<그림 13>
<그림 10>에서 위로 블록을 이동시키면 <그림 11>의 상태가 된다.

<그림 12>의 경우에 위로 블록을 이동시키면 <그림 13>의 상태가 되는데,
그 이유는 한 번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없기 때문이다.


<그림 14>	<그림 15>
마지막으로, 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.
예를 들어, 위로 이동시키는 경우에는 위쪽에 있는 블록이 먼저 합쳐지게 된다. <그림 14>의 경우에 위로 이동하면 <그림 15>를 만든다.

이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다.
보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다.
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고,
1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.

예제 입력 1
3
2 2 2
4 4 4
8 8 8
예제 출력 1
16
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: clrmt noorycode
문제의 오타를 찾은 사람: doju
'''

'''
def find(set, n):
    if set[n] == n:
        return n
    else:
        set[n] = find(set,n)
        return set[n]

def union(set,n,m):
    if find(set,n) != find(set,m):
        set[m] = n

'''
'''
for i in range(N):
    for j in range(N):
        
'''
'''
Move function Pseudo code

Node{
up,down,left,right(Node),
pos,
val,
}

while(curNode):
    if prevNode.val == 0:
        curNode.pos = prevNode.pos
    elif prevNode.val == curNode.val and prevNode.flg == True:
        prevNode.val *= 2
        curNode.val = prevNode.val
        curNode.pos = prevNode.pos
    else:
        curNode.pos = prevNode.pos + 1

        curNode = nextNode
'''
from sys import stdin
input = stdin.readline
LIMIT = 5
UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)
def move(direction):
    pass

# disjoint -> 축소과정 간소화 가능
def moveDown(blocks,blocks_vals):
    disjoint = {v:v-1 for v in range(N) if (v,j) in blocks}
    pass

def moveDown(blocks, block_vals):
    new_blocks = set()
    new_block_vals = dict()
    for j in range(N):
        i = 1
        while i < N:
            if (i-1,j) in blocks and block_vals[i-1,j] == block_vals[i,j] and (i-1,j) not in new_blocks:


    pass

def moveUp(direction):

    pass


def moveLeft(direction):
    pass

def moveRight(direction):
    pass

def dfs(d,board):
    if d == LIMIT:
        return max(zip(*board))
    else:
        res = 0
        for direct in (UP,RIGHT,LEFT,DOWN):
            new_blocks = clearBlock(blocks,direct)
            res = max(res,dfs(d+1,newBlocks))
        return res

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
# blocks = set()
