import sys

sys.stdin = open('input.txt')

T = int(input())

def pascal(N):
    dp = []                                         # 각 행을 담은 리스트 dp에 저장
    for i in range(N):
        arr = []                                    # 각 행을 담을 리스트
        for j in range(i+1):
            if j == 0 or j == i:                    # j 가 0 이거나 j == i 일때는 리스트에 1 추가
                arr.append(1)
            else:
                pas = dp[i-1][j-1] + dp[i-1][j]     # 아닐 때, 합을 구해준다.
                arr.append(pas)
        dp.append(arr)                              # dp 에 각 행을 저장
    return dp

for tc in range(1, T + 1):
    N = int(input())
    dp = pascal(N)
    print(f'#{tc} ')
    for i in dp:
        print(*i)




