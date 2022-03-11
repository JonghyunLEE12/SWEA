import sys
from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, input().split())

graph = [ list(map(int,input())) for _ in range(N)]

def bfs(r,c):
    # 델타 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    queue = deque()
    queue.append((r,c))
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]

            if 0 > new_r or 0 > new_c or new_r >= N or new_c >= M:
                continue

            if graph[new_r][new_c] == 0:
                continue

            if graph[new_r][new_c] == 1:
                graph[new_r][new_c] = graph[r][c] + 1
                queue.append((new_r,new_c))

    return graph[N-1][M-1]

print(bfs(0,0))


