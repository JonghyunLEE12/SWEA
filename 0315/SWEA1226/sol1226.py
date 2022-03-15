import sys
from collections import deque
sys.stdin = open('input.txt')

T = 10

def find_2():
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 2:
                r,c = i,j
    return (r,c)

def bfs():
    queue = deque()
    queue.append((r,c))
    # 델타 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while queue:
        row,col = queue.popleft()
        for i in range(4):
            new_r = row + dr[i]
            new_c = col + dc[i]
            if 0 > new_r or 0 > new_c or new_r >= 16 or new_c >= 16:
                continue
            if matrix[new_r][new_c] == 1:
                continue
            if matrix[new_r][new_c] == 0:
                stack[new_r][new_c] = 1
                matrix[new_r][new_c] = matrix[new_r][new_c] + 1
                queue.append((new_r,new_c))

            if matrix[new_r][new_c] == 3:
                return 1



    return 0

for tc in range(1, T + 1):
    N = int(input())
    matrix = [ list(map(int,input())) for _ in range(16)]

    r,c = find_2()
    stack = [[0]*len(matrix) for _ in range(len(matrix))]
    print(f'#{tc} {bfs()}')

