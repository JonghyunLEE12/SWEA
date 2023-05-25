n,m = map(int,input().split(' '))
matrix = [ list(map(int,input().split(' '))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


dp = [[-1e10] * m for _ in range(n)]
left = [[-1e10] * m for _ in range(n)]
right = [[-1e10] * m for _ in range(n)]


dp[0][0] = matrix[0][0]

# 첫줄 작업
for j in range(1,m):
    dp[0][j] = dp[0][j-1] + matrix[0][j]


for i in range(1,n):
    #2 왼쪽 -> 오른쪽

    left[i][0] = dp[i-1][0] + matrix[i][0]

    for j in range(1,m):
        left[i][j] = max(dp[i-1][j] + matrix[i][j], left[i][j-1]+matrix[i][j])
    

    right[i][m-1] = dp[i-1][m-1] + matrix[i][m-1]

    for j in range(m-2,-1,-1):
        right[i][j] = max(dp[i-1][j] + matrix[i][j], right[i][j+1] + matrix[i][j])
    
    for j in range(m):
        dp[i][j] = max(right[i][j], left[i][j])


print(dp[n-1][m-1])



