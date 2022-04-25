from collections import deque
from copy import deepcopy


# Delta : 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(row,col):
    queue = deque()
    queue.append((row,col))
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0<= nc < n:
                if copy_matrix[nr][nc] != 0 and visited[nr][nc] == 0:
                    queue.append((nr,nc))
                    visited[nr][nc] = 1



n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
max_cnt = 0

for height in range(0,101):
    copy_matrix = deepcopy(matrix)
    visited = [[0]*n for _ in range(n)]

    # 침수 되는 곳
    for i in range(n):
        for j in range(n):
            if copy_matrix[i][j] <= height:
                copy_matrix[i][j] = 0

    # 영역 구하기
    cnt = 0
    for a in range(n):
        for b in range(n):
            if copy_matrix[a][b] != 0 and visited[a][b] == 0:
                cnt+= 1
                visited[a][b] = 1
                bfs(a,b)
    max_cnt = max(max_cnt,cnt)

print(max_cnt)