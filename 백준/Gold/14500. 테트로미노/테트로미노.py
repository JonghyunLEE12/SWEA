N,M = map(int,input().split(' '))

matrix = [list(map(int,input().split(' '))) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c,idx,total):
    global ans
    if ans >= total + maxVal * (3 - idx):
        return
    if idx == 3:
        ans = max(ans,total)
        return
    else:
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if idx == 1:
                    visited[nr][nc] = 1
                    dfs(r,c,idx+1,total+matrix[nr][nc])
                    visited[nr][nc] = 0
                visited[nr][nc] = 1
                dfs(nr,nc,idx+1,total+matrix[nr][nc])
                visited[nr][nc] = 0
                
ans = 0
maxVal = max(map(max,matrix))

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r,c,0,matrix[r][c])
        visited[r][c] = 0

print(ans)