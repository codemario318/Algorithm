'''
직사각형 네개의 합집합의 면적 구하기 출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	4414	3432	3087	78.750%
문제
평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.

이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.



입력
입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다. 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다. 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.

출력
첫 줄에 네개의 직사각형이 차지하는 면적을 출력한다.

예제 입력 1 
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
예제 출력 1 
26
출처
Olympiad > 한국정보올림피아드 > KOI 1996 > 초등부 3번
'''
from sys import stdin
readline = stdin.readline
N = 4


def get_area(lbx, lby, rtx, rty):
    return set([(i, j) for j in range(lby, rty) for i in range(lbx, rtx)])


def main():
    areas = set()

    for _ in range(N):
        lbx, lby, rtx, rty = map(int, readline().split())
        area = get_area(lbx, lby, rtx, rty)
        areas.update(area)

    print(len(areas))


if __name__ == '__main__':
    main()
