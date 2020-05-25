"""
문제 설명
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 빨간색으로 칠해져 있고 모서리는 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

image.png

Leo는 집으로 돌아와서 아까 본 카펫의 빨간색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 빨간색 격자의 수 red가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
빨간색 격자의 수 red는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

"""
brown = 10
red = 2

brown =8
red = 1

def grid_size(grid_num):

    for x in range(1,red+1):
        for y in range(1,x+1):
            if x * y == red and (2+x)*(2+y) == red+brown:
                return [2+x, 2+y]
            elif x * y > red:
                break
#
# def solution(brown, red):
#     carpets = grid_size(brown + red)
#     red_grids = grid_size(red)
#
#     if len(carpets) == 1:
#         return carpets[0]
#
#     for carpet in carpets:
#         for red_size in red_grids:
#             edge = (carpet[0] - red_size[0], carpet[1] - red_size[1])
#             if edge[0] > 1 and edge[1] > 1 and edge[0] % 2 == 0 and edge[1] % 2 == 0:
#                 return carpet
# list(range(10,0,-1))
list(range(1,0,-1))

def solution(brown, red):
    for x in range(1,red+1):
        for y in range(1,x+1):
            if x * y == red and (2+x)*(2+y) == red+brown:
                return [2+x, 2+y]
            elif x * y > red:
                break

solution(8,1)
solution(10,2)
solution(24,24)
solution(5000,4)
grid_size(1)
grid_size(24)
grid_size(3)
grid_size(15)
# grid_size(1)
