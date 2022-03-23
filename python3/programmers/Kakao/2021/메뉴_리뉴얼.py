from itertools import combinations
from collections import Counter

MIN_ORDER = 2

def solution(orders, course):
    answer = []
    setMenus = {n: Counter() for n in course}

    for order in orders:
        for n in course:
            if n > len(order):
                break

            combMenus = combinations(order, n)
            combMenus = map(lambda menu: ''.join(sorted(menu)), combMenus)

            setMenus[n].update(combMenus)

    for menus in setMenus.values():
        if len(menus) == 0:
            continue

        sortedMenu = menus.most_common()
        menu, maxCount = sortedMenu[0]

        if maxCount < MIN_ORDER:
            continue

        answer.append(menu)

        for menu, count in sortedMenu[1:]:
            if maxCount > count:
                break
            answer.append(menu)

    answer.sort()

    return answer 

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	,[2,3,4]	)
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	, [2,3,5]	)
solution(["XYZ", "XWY", "WXA"]	, [2,3,4]	)
