'''
신입 사원

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	69948	24926	18105	33.985%
문제
언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.

그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

출력
각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.

예제 입력 1
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
예제 출력 1
4
3
출처
ICPC > Regionals > Asia Pacific > Korea > Nationwide Internet Competition > Seoul Nationalwide Internet Competition 2006 D번

문제의 오타를 찾은 사람: apjw6112
잘못된 데이터를 찾은 사람: jh05013
데이터를 추가한 사람: xkdlaldfjtnl
'''
from sys import stdin

readline = stdin.readline


def solution(ranks):
    _, prev_rank, *ranks = ranks
    count = 1

    for rank in ranks:
        if prev_rank > rank:
            count += 1
            prev_rank = rank

    return count


if __name__ == '__main__':
    T = int(readline())

    for _ in range(T):
        N = int(readline())
        ranks = [0 for _ in range(N + 1)]

        for _ in range(N):
            r_rank, i_rank = map(int, readline().split())
            ranks[r_rank] = i_rank

        print(solution(ranks))
