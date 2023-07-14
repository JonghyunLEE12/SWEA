'''
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
'''

from collections import deque

n,m = map(int,input().split(' '))
matrix = [ list(map(int,input().split(' '))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c):

    cnt = 1

    queue = deque()
    queue.append([r,c])
    visited[r][c] = 1

    while queue:
        row,col = queue.popleft()
        for i in range(len(dr)):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == 0 and matrix[nr][nc] == 1:
                    visited[nr][nc] = 1
                    queue.append([nr,nc])
                    cnt += 1
    
    return  cnt

rlt = []

for r in range(n):
    for c in range(m):
        if matrix[r][c] == 1 and visited[r][c] == 0:
            rlt.append(bfs(r,c))


if len(rlt) == 0:
    print(0)
    print(0)
else:
    print(len(rlt))
    print(max(rlt))