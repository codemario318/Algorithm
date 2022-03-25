from bisect import bisect_left
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    result = []
    filteredUserScores = defaultdict(list)
    
    for i, values in enumerate(info):
        *options, score = values.split(' ')

        for j in range(1, len(options)+1):
            for option in combinations(options, j):
                filteredUserScores[option].append(int(score))

        filteredUserScores[()].append(score)

    for key in filteredUserScores:
        filteredUserScores[key].sort()

    for q in query:
        *q, score = q.split()
        score = int(score)
        
        q = tuple(filter(lambda x: x != '-' and x != 'and', q))

        users = filteredUserScores[q]         
        userCount = len(users) - bisect_left(users, score)

        result.append(userCount)

    return result

r = solution(
    ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	,
    # ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	
    ["- and - and - and - 150"]	
)

print(r)

list(filter(lambda x: x != '-' and x != 'and', "- and - and - and - 150".split()))
tuple([])