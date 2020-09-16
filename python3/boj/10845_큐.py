'''
큐 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	256 MB	38350	17910	13861	49.179%
문제
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1
15
push 1
push 2
front
back
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
front
예제 출력 1
1
2
2
0
1
2
-1
0
1
-1
0
3
출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: compro0317
'''
from sys import stdin

class Item:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None

    def __len__(self):
        return self.size

    def isEmpty(self):
        return 0 if len(self) else 1

    def getFront(self):
        return self.front.val if self.front else -1

    def getBack(self):
        return self.back.val if self.back else -1

    def push(self, val):
        item = Item(val, None)

        if self.isEmpty():
            self.front = item
            self.back = item
        else:
            self.back.next = item
            self.back = item

        self.size +=1

    def pop(self):
        if self.isEmpty():
            return -1

        temp = self.front

        if len(self) == 1:
            self.front = None
            self.back = None
        else:
            self.front = temp.next

        self.size -= 1

        return temp.val

def solution(queue, cmd):
    if cmd[0] == 'push':
        val = int(cmd[1])
        queue.push(val)
    elif cmd[0] == 'pop':
        print(queue.pop())
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(queue.isEmpty())
    elif cmd[0] == 'front':
        print(queue.getFront())
    elif cmd[0] == 'back':
        print(queue.getBack())

def main():
    N = int(stdin.readline())
    queue = Queue()

    for _ in range(N):
        cmd = stdin.readline().split()
        solution(queue, cmd)

if __name__ == '__main__':
    main()
