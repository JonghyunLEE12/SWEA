# def solution(expression):
#     answer = 0
    
#     num = ''
#     lst = []
#     for ex in expression:
#         if ex in ['+','-','*']:
#             lst.append(num)
#             lst.append(ex)
#             num = ''
#         else:
#             num += ex
    
#     if len(num) != 0:
#         lst.append(num)
#         num = ''
    
    
#     rlt = 1e10
#     visited = [0] * len(lst)
    
#     def dfs(sum_num,start):
        
        
#         for i in range(start,len(lst)):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 dfs(sum_num,i)
#                 visited[i] = 0
    
#     for i in range(len(lst)):
#         if visited[i] == 0:
#             if 
#             visited[i] = 1
#             dfs(sum_num,i)
#             visited[i] = 0
    
#     return answer




from itertools import permutations
def solution(expression):
    symbol = ['+', '-', '*']
    answer = []
    for per in permutations(symbol):
        f, s = per[0], per[1]
        lst = []
        for e in expression.split(f):
            temp = [f"({i})" for i in e.split(s)]
            lst.append(f'({s.join(temp)})')
        answer.append(abs(eval(f.join(lst))))
    return max(answer)
