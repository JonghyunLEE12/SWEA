import sys

sys.stdin = open('input.txt')

T = int(input())

from collections import deque


def bfs(r,c):
    global cnt
    # 델타
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    queue = deque()
    queue.append((r,c))
    while queue:
        row,col = queue.popleft()
        for i in range(4):
            new_r = row + dr[i]
            new_c = col + dc[i]
            if 0<= new_r < n and 0<= new_c < n and (matrix[new_r][new_c] - matrix[row][col] == 1):
                cnt += 1
                queue.append((new_r,new_c))


for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    max_cnt = 0
    room = 10000000
    for r in range(n):
        for c in range(n):
            cnt = 1
            # 델타
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            queue = deque()
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                for i in range(4):
                    new_r = row + dr[i]
                    new_c = col + dc[i]
                    if 0 <= new_r < n and 0 <= new_c < n and (matrix[new_r][new_c] - matrix[row][col] == 1):
                        cnt += 1
                        queue.append((new_r, new_c))

            if cnt > max_cnt:
                max_cnt = cnt
                room = matrix[r][c]
            elif cnt == max_cnt:
                if matrix[r][c] < room:
                    room = matrix[r][c]

    print(f'#{tc} {room} {cnt}')

