'''
멀티탭 스케줄링

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	38590	11150	8138	29.174%
문제
기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다. 준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다. 그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.

예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면,

키보드
헤어드라이기
핸드폰 충전기
디지털 카메라 충전기
키보드
헤어드라이기
키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다.

입력
첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다.

출력
하나씩 플러그를 빼는 최소의 횟수를 출력하시오.

예제 입력 1
2 7
2 3 2 3 1 2 7
예제 출력 1
2
출처
ICPC > Regionals > Asia Pacific > Korea > Nationwide Internet Competition > Seoul Nationalwide Internet Competition 2007 B번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: cloudest, gotlou8317, jimi1017

- 멀티탭에 빈 자리가 있다면 그냥 꼽기
- 빈자리가 없다면
-- 플러그 중 앞으로 사용하지 않을 기기가 있다면 뽑기
-- 모든 기기가 나중에 다시 사용된다면, 가장 나중에 사용될 기기의 플러그 뽑기
'''

from sys import stdin
from collections import deque


def get_next_use(sequence):
    next_use = {}

    for i, device in enumerate(sequence):
        if device not in next_use:
            next_use[device] = deque()
        next_use[device].append(i)

    return next_use


def solution(plug_count, sequence):
    n = len(sequence)

    next_use = get_next_use(sequence)
    multitap = set()
    count = 0

    for device in sequence:
        if device in multitap:
            next_use[device].popleft()
            continue

        if len(multitap) < plug_count:
            multitap.add(device)
            next_use[device].popleft()
            continue

        device_to_remove = None
        furthest_use = -1

        for plugged in multitap:
            if not next_use[plugged]:
                device_to_remove = plugged
                break

            if next_use[plugged][0] > furthest_use:
                furthest_use = next_use[plugged][0]
                device_to_remove = plugged

        multitap.remove(device_to_remove)
        multitap.add(device)
        next_use[device].popleft()
        count += 1

    return count


if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    sequence = list(map(int, stdin.readline().split()))

    print(solution(N, sequence))
