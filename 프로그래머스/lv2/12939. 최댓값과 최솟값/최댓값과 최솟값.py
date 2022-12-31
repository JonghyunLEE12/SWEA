def solution(s):
    answer = ''
    s = s.split(' ')
    new_s = []
    for i in s:
        new_s.append(int(i))
    
    answer = str(min(new_s)) + ' ' + str(max(new_s))
    return answer