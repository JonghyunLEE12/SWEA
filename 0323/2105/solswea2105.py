import sys
import pprint
sys.stdin = open('input.txt')


T = int(input())

# 대각선 델타
dr = [1,1,-1,-1]
dc = [1,-1,-1,1]

def dfs(d,r,c,cnt):
    new_r = r + dr[d]
    new_c = c + dc[d]
    if 0<= new_r < N and 0<= new_c < N and visited[matrix[new_r][new_c]] == 0:
        visited[matrix[new_r][new_c]] = 1
        recur(d,new_r,new_c,cnt+1,1)
        visited[matrix[new_r][new_c]] = 0

def recur(cur,r,c,cnt,move):
    global max_cnt
    if cur == 3 and i == r:
        max_cnt = max(max_cnt,cnt)
        return
    if cur == 2 and max_cnt > cnt * 2:
        return
    if cur == 2 and i + j  == r + c:
        recur(cur+1,r,c,cnt,0)
        return
    dfs(cur,r,c,cnt)
    if cur < 2 and move:
        recur(cur+1,r,c,cnt,0)



for tc in range(1, T + 1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0

    visited = [ 0 for _ in range(101) ]
    for i in range(N):
        for j in range(N):
            recur(0,i,j,0,0)
    if max_cnt == 0:
        max_cnt = -1
    print(f'#{tc} {max_cnt}')

