# def solution(participant, completion):
#     answer = ''
#     participant = sorted(participant)
#     completion = sorted(completion)
    
        
#     for i in range(len(completion)):
#         participant.remove(completion[i])
    
#     answer = participant[0]
#     return answer

import collections
def solution(p, c):
    p.sort()
    c.sort()
    result = collections.Counter(p) - collections.Counter(c)
    
    return list(result)[0]
