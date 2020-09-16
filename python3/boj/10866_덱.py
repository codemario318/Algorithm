'''
덱 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	256 MB	17045	8778	7455	55.386%
문제
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
예제 출력 1
2
1
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
22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back
예제 출력 2
-1
-1
-1
-1
1
1
2
2
333
10
10
333
20
1234
1234
20
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: jh05013
문제의 오타를 찾은 사람: sungjune222
'''
from sys import stdin

class Item:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None

    def push_front(self, val):
        item = Item(val, None, None)

        if self.isEmpty():
            self.back = item
        elif len(self) == 1:
            item.next = self.back
            self.back.prev = item
        else:
            item.next = self.front
            self.front.prev = item

        self.front = item
        self.size += 1

    def push_back(self, val):
        item = Item(val, None, None)

        if self.isEmpty():
            self.front = item
        elif len(self) == 1:
            item.prev = self.front
            self.front.next = item
        else:
            item.prev = self.back
            self.back.next = item

        self.back = item
        self.size += 1

    def _single_pop(self):
        self.front = None
        self.back = None

    def pop_front(self):
        if self.isEmpty():
            return -1

        temp = self.front

        if len(self) == 1:
            self._single_pop()
        else:
            self.front = temp.next

        self.size -= 1

        return temp.val

    def pop_back(self):
        if self.isEmpty():
            return -1

        temp = self.back

        if len(self) == 1:
            self._single_pop()
        else:
            self.back = temp.prev

        self.size -= 1

        return temp.val

    def __len__(self):
        return self.size

    def isEmpty(self):
        return 0 if len(self) else 1

    def getFront(self):
        return -1 if self.isEmpty() else self.front.val

    def getBack(self):
        return -1 if self.isEmpty() else self.back.val

def solution(deque,cmd):
    if cmd[0] == 'push_back':
        val = int(cmd[1])
        deque.push_back(val)
    elif cmd[0] == 'push_front':
        val = int(cmd[1])
        deque.push_front(val)
    elif cmd[0] == 'pop_back':
        print(deque.pop_back())
    elif cmd[0] == 'pop_front':
        print(deque.pop_front())
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        print(deque.isEmpty())
    elif cmd[0] == 'front':
        print(deque.getFront())
    elif cmd[0] == 'back':
        print(deque.getBack())

def main():
    N = int(stdin.readline())
    dq = Deque()

    for _ in range(N):
        cmd = stdin.readline().split()
        solution(dq,cmd)

if __name__ == '__main__':
    main()
