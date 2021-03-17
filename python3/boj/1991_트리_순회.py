'''
트리 순회 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	22590	14011	10671	63.454%
문제
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.



예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

예제 입력 1 
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
예제 출력 1 
ABDCEFG
DBAECFG
DBEGFCA
알고리즘 분류
보기

'''

from sys import stdin

readline = stdin.readline


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node):
        self.root = node

    def add(self, target, left, right):
        parant = self._find(self.root, target)
        parant.left = left
        parant.right = right

    def _find(self, parant, target):
        if parant.val == target:
            return parant

        left = self._find(parant.left, target) if parant.left else None

        if left and left.val == target:
            return left

        right = self._find(parant.right, target) if parant.right else None

        if right and right.val == target:
            return right

    def preorder(self):
        self._pre(self.root)
        print()

    def _pre(self, node):
        if node:
            print(node.val, end='')
            self._pre(node.left)
            self._pre(node.right)

    def inorder(self):
        self._in(self.root)
        print()

    def _in(self, node):
        if node:
            self._in(node.left)
            print(node.val, end='')
            self._in(node.right)

    def postorder(self):
        self._post(self.root)
        print()

    def _post(self, node):
        if node:
            self._post(node.left)
            self._post(node.right)
            print(node.val, end='')


def get_tree(nodes):
    tree = Tree(Node('A'))

    for v, l, r in nodes:
        left = Node(l) if l != '.' else None
        right = Node(r) if r != '.' else None

        tree.add(v, left, right)

    return tree


if __name__ == '__main__':
    n = int(readline())
    nodes = [readline().split() for _ in range(n)]
    nodes.sort()

    tree = get_tree(nodes)

    tree.preorder()
    tree.inorder()
    tree.postorder()
