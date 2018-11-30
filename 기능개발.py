# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 유지된 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	return
# [498,501,470,489]	[2,1,1,0]
# 입출력 예 설명
# 1초 시점의 ₩498은 2초간 가격을 유지하고, 3초 시점에 ₩470으로 떨어졌습니다.
# 2초 시점의 ₩501은 1초간 가격을 유지하고, 3초 시점에 ₩470으로 떨어졌습니다.
# 3초 시점의 ₩470은 최종 시점까지 총 1초간 가격이 떨어지지 않았습니다.
# 4초 시점의 ₩489은 최종 시점까지 총 0초간 가격이 떨어지지 않았습니다.

def solution(progresses, speeds):
    answer = []
    days = [divmod(100 - progresses[x],speeds[x])[0] if divmod(100 - progresses[x],speeds[x])[1] == 0 else divmod(100 - progresses[x],speeds[x])[0]+1 for x in range(len(progresses))]
    days.reverse()
    flow_time = days[-1]
    count = 0
    while len(days) != 0:
        if days[-1] - flow_time <=0:
            count +=1
            days.pop()

            if len(days) == 0:
                answer.append(count)
        else :
            answer.append(count)
            count = 0
            flow_time += days[-1] - flow_time

    return answer
