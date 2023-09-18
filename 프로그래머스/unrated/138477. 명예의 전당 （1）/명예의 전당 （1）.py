def solution(k, score):
    answer = []
    rank = []
    
    for s in score:
        rank.append(s)
        rank.sort(reverse = True)
        
        if len(rank) > k:
            # rank에서 k번째 수 밀어내기
            rank.pop()
            answer.append(min(rank))
        else:
            answer.append(min(rank))
    return answer