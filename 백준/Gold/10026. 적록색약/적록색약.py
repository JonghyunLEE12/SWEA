'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''

from collections import deque


# 델타 상하좌우
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
            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc] == 0 and matrix[r][c] == matrix[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr,nc))

n = int(input())
matrix = [ list(map(str,input().rstrip(' '))) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
# 일반인
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j)
            cnt += 1

## 적녹색양은 r,g 구분 못해

for a in range(n):
    for b in range(n):
        if matrix[a][b] == 'G':
            matrix[a][b] = 'R'


# 적녹색약 방문 새로 만들기
# cnt 도 새로 만들어야지

visited = [[0]*n for _ in range(n)]
b_cnt = 0
for x in range(n):
    for y in range(n):
        if visited[x][y] == 0:
            visited[x][y] = 1
            bfs(x,y)
            b_cnt += 1

print(cnt,b_cnt)