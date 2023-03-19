n = int(input())
matrix = [ list(map(int,input().split(' '))) for _ in range(n)]
answer = 0

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

dp = [[0]*n for _ in range(n)]


def dfs(r,c):
    if dp[r][c]: return dp[r][c]

    dp[r][c] = 1
    for i in range(len(dr)):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n:
            if matrix[nr][nc] > matrix[r][c]:
                dp[r][c] = max(dp[r][c] , dfs(nr,nc)+1)

    return dp[r][c]

for i in range(n):
    for j in range(n):
        answer = max(answer,dfs(i,j))

print(answer)