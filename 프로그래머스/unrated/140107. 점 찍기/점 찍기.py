# from collections import deque

# def solution(k, d):
#     answer = 0
    
#     matrix = [ [0]*(d*2) for _ in range((d*2))]
#     visited = [ [0]*len(matrix[0]) for _ in range(len(matrix))]

#     start_r = int(len(matrix[0]) / 2)
#     start_c = int(len(matrix) / 2)
    
    
#     # 델타 상 하 좌 우
#     dr = [-1,1,0,0]
#     dc = [0,0,-1,1]
    
#     def bfs(row,col):
#         count = 1
#         queue = deque()
#         queue.append([row,col])
#         visited[row][col] = 1
        
#         while queue:
#             r,c = queue.popleft()
#             for i in range(len(dr)):
#                 nr = r + dr[i]*k
#                 nc = c + dc[i]*k
                
#                 if 0 <= nr < len(matrix[0]) and 0 <= nc < len(matrix):
#                     if visited[nr][nc] == 0:
#                         visited[nr][nc] = 1
#                         count += 1
#                         queue.append([nr,nc])
#         print(visited)
#         return count
                        
    
    
#     print(bfs(start_r,start_c))
#     return answer


import math
def solution(k, d):
    answer = 0
    # x 기준으로 세기
    for x in range(0, d + 1, k):
        res_d = math.floor(math.sqrt(d*d - x*x))
        answer += (res_d // k) + 1
    return answer