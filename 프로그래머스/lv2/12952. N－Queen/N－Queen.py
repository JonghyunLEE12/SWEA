# from collections import deque

# # Queen 은 상 하 대각선으로 이동 가능
# dr = [-1,1,0,0,1,-1,1,-1]
# dc = [0,0,-1,1,1,-1,-1,1]

# answer = 0
# def check(row,col,matrix,visited):
#     for i in range(1,len(matrix)):
#         for j in range(len(dr)):
#             nr = row + dr[j] * i
#             nc = col + dc[j] * i
#             if 0 <= nr < len(matrix) and 0<= nc < len(matrix):
#                 if visited[nr][nc] == 0:
#                     visited[nr][nc] = 1

# def dfs(row,col,matrix,visited,cnt):
#     if cnt <= len(visited):
#         answer += 1
#     elif cnt > len(visited):
#         return cnt
#     else:
#         check(row,col,matrix,visited)
#         for i in range(len(matrix)):
#             dfs(cnt,i,matrix,visited,cnt+1)
                    
    
#     return

# def solution(n):
#     global answer
#     matrix = [[0]*n for _ in range(n)]
    
#     for i in range(n):
#         visited = [[0]*n for _ in range(n)] 
#         visited[0][i] = 1
#         dfs(0,i,matrix,visited,1)
#     return answer


def dfs(queen, n, row):
    count = 0
    
    if n == row:
        return 1
    
    # 가로로 한번만 진행
    for col in range(n):
        queen[row] = col

        # for-else구문
        for x in range(row):
            # 세로로 겹치면 안됨
            if queen[x] == queen[row]: 
                break
                
            # 대각선으로 겹치면 안됨
            if abs(queen[x]-queen[row]) == (row-x):
                break
        else:
            count += dfs(queen, n, row+1)
            
    return count

def solution(n):
    queen = [0]*n
        
    return dfs(queen, n, 0)