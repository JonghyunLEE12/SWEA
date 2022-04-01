import sys

sys.stdin = open('input.txt')

T = int(input())


def dfs(y,sum):
    global rlt

    if y == n:
        if rlt > sum:
            rlt = sum
        return

    if rlt < sum:
        return

    for x in range(n):
        if not visited[x]:
            visited[x] = 1
            dfs(y+1 , sum + data[y][x])
            visited[x] = 0


for tc in range(1, T + 1):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]
    visited = [0] * n
    rlt = float('inf')

    dfs(0,0)
    
    print(f'#{tc} {rlt}')

