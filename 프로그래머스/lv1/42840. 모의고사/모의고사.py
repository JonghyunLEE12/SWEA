def solution(answers):
    answer = []
    count1,count2,count3 = 0,0,0
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    for num in range(len(answers)):
        if num1[num % len(num1)] == answers[num]:
            count1 += 1
        if num2[num % len(num2)] == answers[num]:
            count2 += 1
        if num3[num % len(num3)] == answers[num]:
            count3 += 1
    
    rlt = max(count1,count2,count3)
    if rlt == count1:
        answer.append(1)
    if rlt == count2:
        answer.append(2)
    if rlt == count3:
        answer.append(3)

    return answer