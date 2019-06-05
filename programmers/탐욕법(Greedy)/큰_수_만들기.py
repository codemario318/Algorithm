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

# from itertools import combinations
# def solution(number, k):
#     return max(map(lambda x:''.join(x),combinations(list(number),len(number)-k)))
#
# def solution(number, k):
#     i = 0
#     numbers = list(number)
#     while k > 0:
#         if i+1 >= len(numbers):
#             numbers.pop()
#             k -= 1
#         elif numbers[i+1] > numbers[i]:
#             numbers.pop(i)
#             k -= 1
#             i = 0
#         else:
#             i += 1
#     return ''.join(numbers)
# '1213'.replace('1','4',1)
# def solution(number, k):
#     i = 0
#     while k > 0:
#         # print(k)
#         if i+1 >= len(number):
#             number = number.replace(number[-1],'',1)
#             k -= 1
#         elif number[i+1] > number[i]:
#             number = number.replace(number[i],'',1)
#             i = 0
#             k -= 1
#         else:
#             i += 1
#     return number
# '9'[-1]
# def search(number,pos,k):
#     temp = pos
#     while k > 0:
#         if number[pos+1] > number[temp]:
#             temp = pos+1
#         pos += 1
#         k -= 1
#     return temp
#
# def solution(number, k):
#     answer = ''
#     nums = len(number)-k
#     prev = 0
#     next = 0
#
#     while nums > len(answer):
#         next = search(number,prev,k)
#         answer += number[next]
#         if prev != next:
#             k -= next - prev
#         prev = next + 1
#     return answer
#
max('12345')
def search(number, k):

    return

def solution(number, k):
    answer = []
    pos = 0
    for _ in range(len(number)-k):
        if k > 0:
            temp = number[pos:pos+k+1]
            i = temp.index(max(temp))
            answer.append(temp[i])
            k -= i
            pos += i+1
        else:
            return ''.join(answer) + number[pos:]

    return ''.join(answer)

def solution(number, k):
    answer = list(number)
    nums = len(number)-k
    pos = 0
    while(len(answer) > nums):
        temp = answer[pos:pos+k+1]
        try:
            idx = temp.index(max(temp))
        except ValueError:
            return ''.join(answer[:nums])

        if idx == 0:
            pos += 1
        else:
            for _ in range(idx):
                answer.pop(pos)
                k -= 1

    return ''.join(answer)

def solution(number, k):
    answer = []
    pos = 0
    nums = len(number)-k
    while(k > 0 and len(answer) < nums):
        print(answer)
        temp = number[pos:pos+k+1]
        i = temp.index(max(temp))
        answer.append(temp[i])
        k -= i
        pos += i+1
    if len(answer) == nums:
        return ''.join(answer)
    else:
        return ''.join(answer) + number[pos:]

def solution(number, k):
    i = 0
    nums = len(number) - k
    answer = list(number)
    while k > 0:
        if i+1 > nums:
            return ''.join(answer[:nums+1])
        if answer[i+1] > answer[i]:
            answer.pop(i)
            i = 0
            k -= 1
        else:
            i += 1
    return ''.join(answer)
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

def solution(number, k):
    s=0
    length=len(number)
    for i in range(k):
        isEnd=True
        for j in range(s,length-1):
            if number[j]<number[j+1]:
                isEnd=False
                number=number[:j]+number[j+1:]
                length-=1#숫자 하나를 제외했으므로 길이 감소
                # 제외된 인덱스에 뒤 인덱스 값이 오므로 인덱스 조정해야 함
                if j>0:#인덱스가 1이상인 경우 인덱스 하나 줄이면 제자리에서 새로 온 값과 다시 비교 가능해짐(위 for문에서 s가 1 증가하므로)
                    s=j-1
                else:#인덱스가 0인 경우 처음부터 다시 비교
                    s=0
                break#작은 수 제외시켰으므로 다음 것 찾기
        if isEnd==True:#문자열 맨 마지막을 제외 시킴
            print('hi')
            number=number[:-1]
            s=j-1#인덱스 하나 줄이기
    return number


print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("4177252841",1))
print(solution("321",1))

s = 0
for i in range(3):
    for j in range(s,5):
        print(i,j)
        if j == 2:
            s = 4
            i = 2
