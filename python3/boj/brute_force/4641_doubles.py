'''
Doubles 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	2195	1465	1288	68.112%
문제
2~15개의 서로 다른 자연수로 이루어진 리스트가 있을 때, 이들 중 리스트 안에 자신의 정확히 2배인 수가 있는 수의 개수를 구하여라.

예를 들어, 리스트가 "1 4 3 2 9 7 18 22"라면 2가 1의 2배, 4가 2의 2배, 18이 9의 2배이므로 답은 3이다.

입력
입력은 여러 개의 테스트 케이스로 주어져 있으며, 입력의 끝에는 -1이 하나 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 2~15개의 서로 다른 자연수가 주어진다. 각 자연수는 100보다 작으며, 리스트의 끝은 0으로 판별한다(0은 리스트에 속하지 않는다).

출력
각 테스트 케이스마다 한 줄에 걸쳐 정답을 출력한다.

예제 입력 1 
1 4 3 2 9 7 18 22 0
2 4 8 10 0
7 5 11 13 1 3 0
-1
예제 출력 1 
3
2
0
'''

from sys import stdin
EXIT = -1


def readline():
    return map(int, stdin.readline().split())


if __name__ == "__main__":
    while True:
        res = 0
        nums = list(readline())
        if nums[0] == -1:
            break
        nums.sort()

        for i in range(1, len(nums)):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                if b == 2*a:
                    res += 1
                    break
                if 2*a < b:
                    break
        print(res)
