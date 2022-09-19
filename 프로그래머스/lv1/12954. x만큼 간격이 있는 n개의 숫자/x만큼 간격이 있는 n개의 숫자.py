def solution(x, n):
    answer = []
    sum_num = x
    while True:
        if len(answer) == n:
            break
        answer.append(sum_num)
        sum_num += x
    return answer