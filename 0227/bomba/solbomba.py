import sys

sys.stdin = open('input.txt')

T = int(input())

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
# 대각선
dx = [-1,1,-1,1]
dy = [-1,1,1,-1]
def sol(arr):
    max_kill = 0
    for r in range(len(arr)):
        for c in range(len(arr)):
            sum_kill_1 = arr[r][c]
            sum_kill_2 = arr[r][c]
            for i in range(1,P+1):
                for k in range(4):
                    new_r = r + dr[k]*i
                    new_c = c + dc[k]*i
                    new_x = r + dx[k]*i
                    new_y = c + dy[k]*i
                    if 0<= new_r < N and 0<= new_c < N:
                        sum_kill_1 += arr[new_r][new_c]
                    if 0<= new_x < N and 0<= new_y < N:
                        sum_kill_2 += arr[new_x][new_y]
                max_kill = max(max_kill,sum_kill_1,sum_kill_2)
    return max_kill

for tc in range(1, T + 1):
    N,P = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N)]
    ans = sol(matrix)
    print(f'#{tc} {ans}')

