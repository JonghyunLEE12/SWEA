
from pprint import pprint

from collections import deque

# 델타
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(i,j,visited):
    queue = deque()
    melting_que = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue:
        r,c = queue.popleft()
        melt_cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0<= nc < m and visited[nr][nc] == 0:
                if matrix[nr][nc] != 0:
                    visited[nr][nc] = 0
                    queue.append((nr,nc))
                else:
                    melt_cnt += 1
        if melt_cnt:
            melting_que.append((i,j,melt_cnt))
    return melting_que

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

year = 0
while True:
    cnt = 0
    year += 1
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                melt = bfs(i,j,visited)
                while melt:
                    m_r , m_c , m = melt.popleft()
                    matrix[m_r][m_c] = max(matrix[m_r][m_c] - m , 0)
    if cnt == 0:
        year = 0
    if cnt > 2:
        break
print(year)