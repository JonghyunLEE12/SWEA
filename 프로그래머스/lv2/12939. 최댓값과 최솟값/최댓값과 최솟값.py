def solution(s):
    answer = ''
    num = list(map(int,s.split(' ')))
    
    answer = f'{min(num)} {max(num)}'
    
    return answer