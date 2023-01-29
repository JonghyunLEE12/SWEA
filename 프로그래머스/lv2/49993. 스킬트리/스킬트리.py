# from collections import deque

# def solution(skill, skill_trees):
#     answer = 0
    
#     def stacking(sk):
#         queue = deque()
#         for s in sk:
#             queue.append(s)
#         return queue
    
    
#     def checking(skill,queue):
#         stack = []

#         for i in range(len(queue)):
#             if queue[i] in skill:
#                 stack.append(queue[i])
        
        
#         skill = list(skill)
        
#         if skill == stack:
#             return True
        
#         print(skill)
#         print(stack)
#         print('####')
        
#         for i in range(len(stack)):
#             if stack[i] != skill[i]:
#                 return False
        
    
#         return False
    
#     for sk in skill_trees:
#         queue = stacking(sk)
        
#         if checking(skill,queue):
#             answer += 1
        
    
#     return answer



def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        s = ""                      # 하나의 스킬트리를 뽑을 때마다 s 초기화
        for ch in skill_tree:       
            if ch in skill:         # 스킬트리 중에 skill이 있다면 s에 추가
                s += ch
        
        if skill[:len(s)] == s:     # 만든 s를 기준으로 skill과 같다면 count += 1
            count += 1
    
    return count