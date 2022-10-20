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
    print(list(result)[0])
    
    return list(result)[0]


# from collections import defaultdict
# def solution(participant,completion):
#     answer = 0
    
#     n_dict = defaultdict(int)
#     for i in participant:
#         n_dict[i] += 1
    
#     for j in completion:
#         n_dict[j]+= 1    
    
#     rlt = []
#     print(n_dict[1])
#     return answer
