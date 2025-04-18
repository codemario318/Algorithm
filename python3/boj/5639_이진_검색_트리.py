'''
이진 검색 트리 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	54092	21478	15156	38.267%
문제
이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.

노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.


전위 순회 (루트-왼쪽-오른쪽)은 루트를 방문하고, 왼쪽 서브트리, 오른쪽 서브 트리를 순서대로 방문하면서 노드의 키를 출력한다. 후위 순회 (왼쪽-오른쪽-루트)는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드 순서대로 키를 출력한다. 예를 들어, 위의 이진 검색 트리의 전위 순회 결과는 50 30 24 5 28 45 98 52 60 이고, 후위 순회 결과는 5 28 24 45 30 60 52 98 50 이다.

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

입력
트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

출력
입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1
50
30
24
5
28
45
98
52
60
예제 출력 1
5
28
24
45
30
60
52
98
50
출처
ICPC > Regionals > Asia Pacific > Thailand > 2011 ACM-ICPC Asia Phuket Regional Programming Contest B번

문제를 번역한 사람: baekjoon
'''

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
readline = stdin.readline


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    root = None

    def push(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        node = Node(value)
        parent = self.root

        while parent:
            if parent.val > value:
                if parent.left is None:
                    parent.left = node
                    return
                parent = parent.left
            else:
                if parent.right is None:
                    parent.right = node
                    return
                parent = parent.right

    def postorder(self):
        if self.root is None:
            return
        self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return

        self._postorder(node.left)
        self._postorder(node.right)
        print(node.val)


if __name__ == '__main__':
    nums = []

    for line in stdin:
        nums.append(int(line))

    tree = Tree()

    for num in nums:
        tree.push(num)

    tree.postorder()
