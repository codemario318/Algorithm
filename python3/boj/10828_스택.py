'''
스택 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	256 MB	69410	26693	19501	39.821%
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
예제 출력 1
2
2
0
2
1
-1
0
1
-1
0
3
예제 입력 2
7
pop
top
push 123
top
pop
top
pop
예제 출력 2
-1
-1
123
123
-1
-1
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: djm03178
알고리즘 분류
보기

메모
메모 작성하기
5
push 1
push 2
push 3
push 4
push 5

'''

from sys import stdin

class Item:
    def __init__(self, val, prev):
        self.val = val
        self.prev = prev

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.isEmpty():
            return 'Stack is Empty'
        else:
            return f'[ {self._get_items(self.top)} ]'

    def _get_items(self, item):
        if item.prev == None:
            return str(item.val)
        else:
            return f'{self._get_items(item.prev)} {item.val}'

    def push(self, val):
        self.top = Item(val, self.top)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            res = self.top.val
            self.top = self.top.prev
            self.size -= 1
            return res

    def isEmpty(self):
        return 0 if len(self) else 1

    def getTop(self):
        if self.isEmpty():
            return -1
        else:
            return self.top.val

def solution(stack, cmd):
    if cmd[0] == 'push':
        val = int(cmd[1])
        stack.push(val)
    elif cmd[0] == 'pop':
        print(stack.pop())
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(stack.isEmpty())
    elif cmd[0] == 'top':
        print(stack.getTop())


def main():
    N = int(stdin.readline())
    stack = Stack()

    for _ in range(N):
        cmd = stdin.readline().split()
        solution(stack, cmd)

if __name__ == '__main__':
    main()
