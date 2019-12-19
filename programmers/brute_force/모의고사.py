"""
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
"""
answers = [1,3,2,4,2]
answers = [1,2,3,4,5]
def solution(answers):
    counts = {1:0,2:0,3:0}
    supo_a = '12345'*(len(answers)//5) + '12345'[:len(answers)%5]
    supo_b = '21232425'*(len(answers)//8) + '21232425'[:len(answers)%8]
    supo_c = '3311224455'*(len(answers)//10) + '3311224455'[:len(answers)%10]

    for i,answer in enumerate(answers):
        if int(supo_a[i]) == answer:
            counts[1] += 1
        if int(supo_b[i]) == answer:
            counts[2] += 1
        if int(supo_c[i]) == answer:
            counts[3] += 1

    keys = sorted(counts,key=lambda x:(counts[x],-x),reverse=True)
    res = [keys[0]]

    for k in keys[1:]:
        if counts[res[0]] == counts[k]:
            res.append(k)
        else:
            return res
    return res
