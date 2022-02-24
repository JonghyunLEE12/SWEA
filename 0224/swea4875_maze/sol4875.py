import sys

sys.stdin = open('input.txt')

T = int(input())

# 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    for k in range(4):
        new_r = r + dr[k]
        new_c = c + dc[k]
        if 0 <= new_r < N and 0 <= new_c < N and not stack[new_r][new_c]:
            if not maze[new_r][new_c]:
                stack[new_r][new_c] = True
                if dfs(new_r,new_c):
                    return True
            elif maze[new_r][new_c] == 3:
                return True

def find_2(maze):

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return 1 if dfs(i,j) else 0
for tc in range(1, T + 1):
    N = int(input())
    maze = [ list(map(int,input())) for _ in range(N) ]
    stack = [[False for _ in range(N)]for _ in range(N) ]
    print(f'#{tc} {find_2(maze)}')

