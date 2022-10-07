# def solution(s):
#     answer = 1
    
#     while True:
#         stack = []
#         if len(s) == 0:
#             break
        
#         for i in range
#     return answer


def solution(s): 
    stack = []
    for i in s:
        if len(stack) == 0: 
            stack.append(i)
        elif stack[-1] == i: 
            stack.pop()
        else: 
            stack.append(i)
    if len(stack) == 0: 
        return 1
    else: 
        return 0 