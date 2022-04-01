import sys

sys.stdin = open('input.txt')

from collections import deque

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [1,-1,0,0]

def bfs(r,c,shark_size):
    distance = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((r,c))
    visited[r][c] = 1
    temp = []
    while queue:
        row,col = queue.popleft()
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0<= nr < n and 0<= nc < n and visited[nr][nc] == 0:
                if matrix[nr][nc] <= shark_size:
                    queue.append((nr,nc))
                    visited[nr][nc] = 1
                    distance[nr][nc] = distance[row][col] + 1

                    if matrix[nr][nc] < shark_size and matrix[nr][nc] != 0:
                        temp.append((nr,nc,distance[nr][nc]))

    return sorted(temp,key=lambda x:(x[2], x[0], x[1]))



n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]


# 상어 위치 = 9 , 사이즈 = 2
r,c,size = 0,0,2
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            r = i
            c = j

cnt = 0
rlt = 0
while True:
    shark = bfs(r,c,size)

    # 엄마 불러
    if len(shark) == 0:
        break
    nr, nc, dist = shark.pop()
    rlt += dist
    matrix[r][c], matrix[nr][nc] = 0,0
    r,c = nr,nc
    cnt += 1            # 먹은 횟수
    if cnt == size:     # 사이즈 증가
        size += 1
        cnt = 0

print(rlt)

