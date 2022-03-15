import sys

sys.stdin = open('input.txt')

from collections import deque
T = int(input())


def find():
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 2:
                r,c = i,j
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            if matrix[a][b] == 3:
                target_r ,target_c = a,b
    return (r,c,target_r,target_c)

def bfs():
    # 델타
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    queue = deque()
    queue.append((r,c))
    while queue:
        row,col = queue.popleft()
        visited[row][col] = True
        for i in range(4):
            new_r = row + dr[i]
            new_c = col + dc[i]
            if 0 <= new_r < n and 0 <= new_c < n and not visited[new_r][new_c] and matrix[new_r][new_c] == 0:
                queue.append((new_r, new_c))
                stack[new_r][new_c] = stack[row][col] + 1
            elif 0 <= new_r < n and 0 <= new_c < n and not visited[new_r][new_c] and matrix[new_r][new_c] == 3:
                stack[new_r][new_c] = stack[row][col]
    return stack[target_r][target_c]

for tc in range(1, T + 1):
    n = int(input())
    matrix = [ list(map(int,input())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    stack = [[0]*n for _ in range(n)]
    r,c,target_r,target_c = find()
    print(f'#{tc} {bfs()}')

