'''
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
'''


n = int(input())
matrix = [ list(map(int,input().split(' '))) for _ in range(n) ]
dp = [ [0]*n for _ in range(n)]

# 시작점
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break

        move = matrix[i][j]
        if i + move < n:
            dp[i+move][j] += dp[i][j]
        
        if j + move < n :
            dp[i][j+move] += dp[i][j]



print(dp[n-1][n-1])
