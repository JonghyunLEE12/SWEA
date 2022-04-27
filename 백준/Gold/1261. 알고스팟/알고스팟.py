import heapq

# 델타 : 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(row,col):
    queue = []
    heapq.heappush(queue,(0,row,col))
    while queue:
        count,r,c = heapq.heappop(queue)
        if (r,c) == (n-1,m-1):
            return count
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < n and 0<= nc < m:
                if visited[nr][nc] == 0:
                    if matrix[nr][nc] == 1:
                        heapq.heappush(queue,(count+1,nr,nc))
                    else:
                        heapq.heappush(queue,(count,nr,nc))
                    visited[nr][nc] = 1


m,n = map(int,input().split())
matrix = [ list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

print(bfs(0,0))