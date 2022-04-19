from collections import deque

# 델타
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(sr,sc,gr,gc):
    queue = deque()
    queue.append((sr,sc))
    matrix[sr][sc] = 1
    while queue:
        r,c = queue.popleft()
        if r == gr and c == gc:
            print(matrix[gr][gc]-1)
            return
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < l and 0 <= nc < l and matrix[nr][nc] == 0 :
                queue.append((nr,nc))
                matrix[nr][nc] = matrix[r][c] + 1



tc = int(input())
for _ in range(tc):
    l = int(input())
    matrix = [[0]*l for _ in range(l)]
    start_r,start_c = map(int,input().split())
    goal_r, goal_c = map(int,input().split())

    bfs(start_r,start_c,goal_r,goal_c)