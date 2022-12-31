from collections import Counter

def solution(k, tangerine):
    answer = 0
    sum = 0
    tan = Counter(tangerine).most_common() #Counter(배열).most_common() ->반복횟수확인
    
    for t in tan:
        sum += t[1]
        answer += 1
        if sum >= k:
            return answer
    
    return answer