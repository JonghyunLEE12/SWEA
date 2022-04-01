import sys

sys.stdin = open('input.txt')

T = int(input())

def dfs(idx,end,rlt):
    global max_num
    if idx == end:
        if rlt > max_num:
            max_num = rlt
        return

    if rlt <= max_num:
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            new_rlt = rlt * matrix[idx][i] * 0.01
            dfs(idx+1,end,new_rlt)
            visited[i] = 0


for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    max_num = -9999999999999
    dfs(0,n,1)
    ans = round(max_num*100 , 6)
    print(f'#{tc} {ans:0.6f}')

