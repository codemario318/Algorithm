from collections import deque

MAX_DIST = 2
OFFSET = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(places):
    return [checkInterviewState(place) for place in places]


def checkInterviewState(place):
    height = len(place)
    width = len(place[-1])

    checkedSheets = [[None for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            sheet = place[i][j]

            if sheet != 'P':
                continue
            
            checkedSheets[i][j] = True
            ruleBreaker = isRuleBreaker(place, i, j, checkedSheets)

            if ruleBreaker:
                return 0

    return 1


def isRuleBreaker(place, i, j, checkedSheets):
    queue = deque([(i+wi, j+wj, MAX_DIST-1) for wi, wj in OFFSET if isInPlace(place, i+wi, j+wj)])

    while queue:
        x, y, remainDist = queue.popleft()

        currentSheet = place[x][y]

        if currentSheet == 'P':
            return True

        if currentSheet == 'X' or remainDist == 0:
            continue

        for wx, wy in OFFSET:
            nx, ny = x + wx, y + wy
            
            if not isInPlace(place, nx, ny) or checkedSheets[nx][ny]:
                continue
            
            checkedSheets[nx][ny] = True
            queue.append((nx, ny, remainDist - 1))

    return False


def isInPlace(place, x, y):
    return  0 <= x < len(place) and 0 <= y < len(place[-1])

res = solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	)

print(res)