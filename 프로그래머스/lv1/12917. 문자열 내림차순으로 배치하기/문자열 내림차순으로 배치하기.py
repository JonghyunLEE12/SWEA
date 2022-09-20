def solution(s):
    answer = ''
    
    words = sorted(s, reverse= True)
    
    for w in words:
        answer += w
    return answer