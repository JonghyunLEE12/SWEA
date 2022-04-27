import heapq
from pprint import pprint
from collections import deque

# Delta 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(row,col):
    queue = []
    heapq.heappush(queue,(0,row,col))
    while queue:
        count, r, c = heapq.heappop(queue)
        if (r,c) == (n-1,n-1):
            return count
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < n and 0<= nc < n:
                if visited[nr][nc] == 0:
                    if matrix[nr][nc] == 0:
                        heapq.heappush(queue,(count+1,nr,nc))
                    else:
                        heapq.heappush(queue,(count,nr,nc))
                    visited[nr][nc] = 1


n = int(input())
matrix = [list(map(int,input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

start_r , start_c = 0,0

rlt = bfs(start_r,start_c)
print(rlt)
