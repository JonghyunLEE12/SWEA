def solution(intStrs, k, s, l):
    answer = []
    
    for num in intStrs:
        num = list(num)
        check = ''.join(num[s:s+l])
        
        if int(check) > k:
            answer.append(int(check))
    return answer