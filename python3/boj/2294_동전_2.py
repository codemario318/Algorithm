'''
동전 2

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	128 MB	85619	26990	19154	30.303%
문제
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

예제 입력 1
3 15
1
5
12
예제 출력 1
3
출처
잘못된 조건을 찾은 사람: apples1309, djm03178
빠진 조건을 찾은 사람: goodcrane3
데이터를 추가한 사람: hayman42, isac322, kory0711, paraworld
'''

from sys import stdin

readline = stdin.readline

if __name__ == '__main__':
    n, k = map(int, readline().split())
    coins = [int(readline()) for _ in range(n)]

    mem = [float('inf') for n in range(k + 1)]
    mem[0] = 0

    for coin in coins:
        for i in range(coin, k + 1):
            if mem[i - coin] < float('inf'):
                mem[i] = min(mem[i], mem[i - coin] + 1)

    print(mem[-1] if mem[-1] < float('inf') else -1)
