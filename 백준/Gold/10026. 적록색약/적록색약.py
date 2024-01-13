'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''

from collections import deque

n = int(input())
matrix = [ list(input()) for _ in range(n) ]
visited = [[0] * len(matrix[0]) for _ in range(n) ]

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]



def bfs(r,c,mark,visited):
    queue = deque()
    queue.append([r,c])
    visited[r][c] = 1

    while queue:
        row,col = queue.popleft()
        for i in range(len(dr)):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                if visited[nr][nc] == 0 and matrix[nr][nc] == mark:
                    queue.append([nr,nc])
                    visited[nr][nc] = 1





# 일반인 구역

cnt = 0

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if visited[r][c] == 0:
            bfs(r,c,matrix[r][c],visited)
            cnt += 1
            

# 적녹색맹 변경

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == 'R':
            matrix[r][c] = 'G'


r_visited = [ [0]*len(matrix[0]) for _ in range(n) ]
r_cnt = 0

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if r_visited[r][c] == 0:
            bfs(r,c,matrix[r][c],r_visited)
            r_cnt += 1

print(cnt,r_cnt)
