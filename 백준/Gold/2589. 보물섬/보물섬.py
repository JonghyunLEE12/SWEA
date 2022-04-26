from collections import deque


# 델타 : 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(row,col):
    queue = deque()
    queue.append((row,col))
    max_n = 0
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0<= nc < m:
                if visited[nr][nc] == 0 and matrix[nr][nc] != 'W':
                    matrix[nr][nc] = matrix[r][c] + 1
                    max_n = max(matrix[nr][nc] , max_n)
                    visited[nr][nc] = 1
                    queue.append((nr,nc))
    return max_n

n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
rlt = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] != 'W':
            visited = [[0]*m for _ in range(n)]
            visited[i][j] = 1
            matrix[i][j] = 0
            rlt= max(bfs(i,j),rlt)

print(rlt)