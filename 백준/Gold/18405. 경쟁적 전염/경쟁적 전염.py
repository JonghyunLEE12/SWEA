from collections import deque

n,k = map(int,input().split(' '))

matrix = []
virus = []

for i in range(n):
    temp = list(map(int,input().split(' ')))
    matrix.append(temp)
    for j in range(n):
        if matrix[i][j] != 0:
            virus.append([matrix[i][j],i,j,0])
    

s,x,y = map(int,input().split(' '))


# 델타 상 하 좌 우

dr = [-1,1,0,0]
dc = [0,0,-1,1]


virus.sort()
queue = deque(virus)

while queue:
    virus,r,c,time = queue.popleft()
    if time == s:
        break
    for i in range(len(dr)):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if matrix[nr][nc] == 0:
                matrix[nr][nc] = virus
                queue.append((virus,nr,nc,time+1))


print(matrix[x-1][y-1])