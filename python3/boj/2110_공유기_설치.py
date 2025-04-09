'''
공유기 설치 실패다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	88116	32510	22367	37.310%
문제
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

예제 입력 1
5 3
1
2
8
4
9
예제 출력 1
3
힌트
공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다.

출처
Olympiad > USA Computing Olympiad > 2004-2005 Season > USACO February 2005 Contest > Gold 3번

데이터를 추가한 사람: ahmg1216, djm03178, hwangyj9
잘못된 데이터를 찾은 사람: fler9617

---

공유기 사이의 거리의 최대값을 구해야하는 문제

이분탐색 적용 가능?
- 최적 공유기 사이의 거리를 mid로
- left = 1, right = max(X) - min(X)
- 첫 번째 집 부터 공유기 설치 > 다음 집이 최소 mid 보다 클 경우 설치 > 반복
- 모든 공유기 설치할 수 있으면 left = mid, 아니면 right = mid


5 3
0
2
4
6
8

4

4 2
0
4
8
12

12
'''

from sys import stdin

readline = stdin.readline


def can_install(distance, homes, router_count):
    count = 1
    last_position = homes[0]

    for home in homes[1:]:
        if home - last_position >= distance:
            count += 1
            last_position = home

    return count >= router_count


def binary_search(router_count, homes):
    left = 1
    right = homes[-1] - homes[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if can_install(mid, homes, router_count):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


if __name__ == '__main__':
    N, C = map(int, readline().split())
    homes = [int(readline()) for _ in range(N)]
    homes.sort()

    print(binary_search(C, homes))
