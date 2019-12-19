'''
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
1924	2	94
1231234	3	3234
4177252841	4	775841
'''
number = '4178'
k= 2
solution(number, k)

number = '1924'
k = 2
solution(number, k)

number = '1231234'
k =	3	#3234
solution(number, k)

number = '4177252841'
k=	4	#775841
solution(number, k)

number = '9177252841'
k=	4	#775841
solution(number, k)

number = '7777777777'
k=	4
solution(number, k)
print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("4177252841",1))
print(solution("321",1))

def solution(number,k):
    answer = []
    i = 0
    while k and i < len(number):
        if not answer or answer[-1] >= number[i]:
            answer.append(number[i])
            i += 1

        else:
            answer.pop()
            k -= 1

    if k != 0:
        return ''.join(answer[:-k])
    elif i < len(number):
        return ''.join(answer)+number[i:]
    # return answer, i,number[i:],k

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("4177252841",1))
print(solution("321",1))
print(solution("77777",3))
print(solution("177777",3))

'77777'[:-2]
