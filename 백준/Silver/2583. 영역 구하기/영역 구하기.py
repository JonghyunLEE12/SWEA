from collections import deque

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(a,b):
    count = 1
    matrix[a][b] = 9
    queue = deque()
    queue.append((a,b))
    while queue:
        row,col = queue.popleft()
        for i in range(len(dr)):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < m and 0<= nc < n:
                if matrix[nr][nc] == 0:
                    matrix[nr][nc] = 9
                    queue.append((nr,nc))
                    count += 1
    return count

    
n,m,k = map(int,input().split())

matrix = [[0]*(n) for _ in range(m)]
visited = [[0]*(n) for _ in range(m)]


for _ in range(k):
    x,y,r,c = map(int,input().split())
    for i in range(y,c):
        for j in range(x,r):
            matrix[j][i] = 9


rlt = []

for a in range(m):
    for b in range(n):
        if matrix[a][b] == 0:
            rlt.append(bfs(a,b))
rlt = sorted(rlt)
# print(rlt)
print(len(rlt))
print(*rlt) 