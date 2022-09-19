def solution(phone_number):
    answer = ''
    reversed_num = phone_number[::-1]

    not_change = reversed_num[0:4]
    change = reversed_num[4:]
    
    for i in change:
        answer += '*'
    answer = not_change + answer
    return answer[::-1]