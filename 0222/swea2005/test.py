for i in range(N):
    arr = []
    for j in range(i + 1):
        if j == 0 or j == i:
            arr.append(1)
            print(1, end='')
        else:
            arr.append(dp[i - 1][j - 1] + dp[i - 1][j])
            print(dp[i - 1][j - 1] + dp[i - 1][j], end='')
    dp.append(arr)
    print()