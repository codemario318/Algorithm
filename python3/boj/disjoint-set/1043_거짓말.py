'''
거짓말

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	39825	18098	14008	45.787%
문제
지민이는 파티에 가서 이야기 하는 것을 좋아한다. 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다. 지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다. 당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다. 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다. 문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다. 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다. 당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다. 지민이는 이런 일을 모두 피해야 한다.

사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다. 그리고 각 파티에 오는 사람들의 번호가 주어진다. 지민이는 모든 파티에 참가해야 한다. 이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.

둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.

셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.

N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

예제 입력 1
4 3
0
2 1 2
1 3
3 2 3 4
예제 출력 1
3
예제 입력 2
4 1
1 1
4 1 2 3 4
예제 출력 2
0
예제 입력 3
4 1
0
4 1 2 3 4
예제 출력 3
1
예제 입력 4
4 5
1 1
1 1
1 2
1 3
1 4
2 4 1
예제 출력 4
2
예제 입력 5
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4
예제 출력 5
4
예제 입력 6
8 5
3 1 2 7
2 3 4
1 5
2 5 6
2 6 8
1 8
예제 출력 6
5
예제 입력 7
3 4
1 3
1 1
1 2
2 1 2
3 1 2 3
예제 출력 7
0
출처
문제를 번역한 사람: baekjoon, doju
잘못된 번역을 찾은 사람: koosaga
'''

from sys import stdin

readline = stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b, truths):
    a = find(parent, a)
    b = find(parent, b)

    if a in truths:
        parent[b] = a
    elif b in truths:
        parent[a] = b
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == '__main__':
    N, M = map(int, readline().split())
    _, *truths = map(int, readline().split())

    truths = set(truths)
    parties = []
    parents = [i for i in range(N + 1)]

    for _ in range(M):
        _, *members = map(int, readline().split())

        parties.append(members)

        master, *members = members

        for member in members:
            union(parents, master, member, truths)

    count = 0

    for members in parties:
        for member in members:
            if find(parents, member) in truths:
                break
        else:
            count += 1

    print(count)
