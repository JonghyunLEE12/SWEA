def solution(array):
    answer = 0
    for word in array:
        for wo in str(word):
            if wo == '7':
                answer += 1
                
    return answer