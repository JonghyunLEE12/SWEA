'''
3
12 -10 70
-20 20 -20
19 100 7
'''
from collections import deque

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c):
    if matrix[r][c] == matrix[n-1][n-1]:
        rlt.append(matrix[r][c])
        return
    queue = deque()
    queue.append((r,c))
    while queue:
        row,col = queue.popleft()
        for i in range(4):
            new_r = row + dr[i]
            new_c = col + dc[i]
            if 0<= new_r < n and 0<= new_c < n:
                visited[new_r][new_c] = True
                queue.append((new_r,new_c))


n = int(input())
matrix = [ list(map(int,input().split())) for _ in range(n)]
visited = [ [False]*n for _ in range(n)]
for r in range(1,n):
    for c in range(1,n):
        rlt = [matrix[0][0]]
        visited[r][c] = True
        bfs(r,c)
        visited[r][c] = False
