'''
6 4
0100
1110
1000
0000
0111
0000
'''
from collections import deque

n,m = map(int,input().split(' '))
matrix = [ list(map(int,input().rstrip(' '))) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

# 델타
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs():
    queue = deque()
    queue.append([0,0,1])
    visited[0][0][1] = 1

    while queue:
        row,col,t = queue.popleft()

        if row == (n-1) and col == (m-1):
            return visited[row][col][t]

        for i in range(len(dr)):

            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if matrix[nr][nc] == 1 and t == 1:
                    visited[nr][nc][0] += visited[row][col][1] + 1
                    queue.append([nr,nc,0])
                
                elif matrix[nr][nc] == 0 and visited[nr][nc][t] == 0:
                    visited[nr][nc][t] += visited[row][col][t] + 1
                    queue.append([nr,nc,t])
    
    return -1
 


print(bfs())





