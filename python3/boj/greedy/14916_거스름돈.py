'''
거스름돈

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	32135	14937	12313	46.878%
문제
춘향이는 편의점 카운터에서 일한다.

손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다. 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.

예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.

입력
첫째 줄에 거스름돈 액수 n(1 ≤ n ≤ 100,000)이 주어진다.

출력
거스름돈 동전의 최소 개수를 출력한다. 만약 거슬러 줄 수 없으면 -1을 출력한다.

예제 입력 1
13
예제 출력 1
5
예제 입력 2
14
예제 출력 2
4
출처
University > 한양대학교 ERICA 캠퍼스 > 2017 ERICA Programming Contest > League B (초보) H번

문제의 오타를 찾은 사람: gdfssd, pkcchoi3
잘못된 조건을 찾은 사람: isku
데이터를 추가한 사람: nandong1104, object1997
'''

from sys import stdin

readline = stdin.readline

if __name__ == '__main__':
    n = int(readline())
    count_five, mod = divmod(n, 5)
    count_two, mod = divmod(mod, 2)

    while mod > 0 and count_five >= 0:
        count_five -= 1
        mod += 5
        div, mod = divmod(mod, 2)
        count_two += div

    if count_five < 0:
        print(-1)
    else:
        print(count_five + count_two)
