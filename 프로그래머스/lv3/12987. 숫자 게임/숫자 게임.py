# def solution(A, B):
#     answer = -1
    
#     max_value = 0
    
    
#     visited = [0] * len(B)
#     rlt = set()
#     def check(arr):
#         cnt = 0
#         for i in range(len(arr)):
#             if arr[i] > A[i]:
#                 cnt += 1
        
#         rlt.add(cnt)
        
    
#     def dfs(start,arr):
#         if len(arr) == len(B):
#             check(arr)
#             return
#         for i in range(len(B)):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 arr.append(B[i])
#                 dfs(start,arr)
#                 arr.pop()
#                 visited[i] = 0
    
#     arr = []
#     for i in range(len(B)):
#         if visited[i] == 0:
#             visited[i] = 1
#             arr.append(B[i])
#             dfs(i,arr)
#             arr.pop()
#             visited[i] = 0
    
#     answer = max(rlt)
#     if answer == 0:
#         return 0
#     return answer

from collections import deque

def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    
    while B:
        if A[0] < B[0]:
            answer += 1
            A.popleft()
            B.popleft()
        else:
            B.popleft()
    
    return answer