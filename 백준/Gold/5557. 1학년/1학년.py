'''
11
8 3 2 4 8 7 2 4 0 8 8
'''

n = int(input())
numbers = list(map(int,input().split(' ')))
dp = [[0]*21 for _ in range(n)]

dp[0][numbers[0]] = 1

# DP 테이블 채우기
for i in range(1, n - 1):
    for cur_num in range(21):
        if dp[i - 1][cur_num] != 0:
            # 더하기 경우
            if 0 <= cur_num + numbers[i] <= 20:
                dp[i][cur_num + numbers[i]] += dp[i - 1][cur_num]
            # 빼기 경우
            if 0 <= cur_num - numbers[i] <= 20:
                dp[i][cur_num - numbers[i]] += dp[i - 1][cur_num]



print(dp[-2][numbers[-1]])

