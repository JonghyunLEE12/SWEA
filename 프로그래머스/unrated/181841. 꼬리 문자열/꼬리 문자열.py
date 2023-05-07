def solution(str_list, ex):
    answer = ''
    
    for sl in str_list:
        if ex in sl:
            continue
        else:
            answer += sl
    return answer