import sys

sys.stdin = open('input.txt')

T = int(input())

# 상하좌우 델타
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 대각선 델타
dx = [-1,1,-1,1]
dy = [-1,1,1,-1]
def sol(arr):
    max_sum = 0
    # 일단 모든 열을 순회
    for r in range(N):
        for c in range(N):
            sum_1 = arr[r][c]
            sum_2 = arr[r][c]
            # 가로,세로,대각선 순회 해야 겠지?
            for i in range(1,P+1):
                for k in range(len(dr)):
                    new_r = r + dr[k]*i
                    new_c = c + dc[k]*i
                    new_x = r + dx[k]*i
                    new_y = c + dy[k]*i
                    # 가로,세로의 합
                    if 0 <= new_r < N and 0 <= new_c < N:
                        sum_1 += arr[new_r][new_c]
                    # 대각선
                    if 0 <= new_x < N and 0 <= new_y < N:
                        sum_2 += arr[new_x][new_y]
                max_sum = max(max_sum,sum_1,sum_2)
    return max_sum

for tc in range(1, T + 1):
    # N x N 행렬 , P는 폭탄의 파워
    N , P = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    ans = sol(matrix)
    print(f'#{tc} {ans}')

