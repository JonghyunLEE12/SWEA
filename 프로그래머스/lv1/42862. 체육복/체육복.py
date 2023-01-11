def solution(n, lost, reserve):
    answer = 0
    
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    cnt = 0
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    cnt = len(set_lost)
    answer = n - cnt 
    return answer