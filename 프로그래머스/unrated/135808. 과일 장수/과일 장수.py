def solution(k, m, score):
    answer = 0
    
    box = []
    rlt = []
    
    score.sort(reverse = True)
    
    def cal(box):
        min_num = min(box)
        rlt.append(min_num*len(box))
        
    for apple in score:
        if len(box) == m:
            cal(box)
            box = [apple]
        else:
            box.append(apple)
    
    if len(box) == m:
        cal(box)
    
    answer = sum(rlt)
    return answer
