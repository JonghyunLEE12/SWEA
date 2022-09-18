def solution(s):
    answer = True
    
    count_p1 = s.count('p')
    count_p2 = s.count('P')
    
    count_p = count_p1 + count_p2
    
    count_y1 = s.count('y')
    count_y2 = s.count('Y')
    
    count_y = count_y1 + count_y2
    
    if count_p != count_y:
        return False
    return True