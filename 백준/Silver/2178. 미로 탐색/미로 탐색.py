'''
4 6
101111
101010
101011
111011
'''

from collections import deque

n,m = map(int,input().split(' '))

matrix = [list(map(str,input().rstrip(' '))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c):
    queue = deque()
    queue.append([r,c])
    visited[r][c] = 1

    while queue:
        row,col = queue.popleft()

        for i in range(len(dr)):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == 0 and matrix[nr][nc] == '1':
                    queue.append([nr,nc])
                    visited[nr][nc] = visited[row][col] + 1

    
    return visited[n-1][m-1]

print(bfs(0,0))