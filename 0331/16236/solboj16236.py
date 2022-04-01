import sys

sys.stdin = open('input.txt')

from collections import deque

# 델타
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(start):
    global shark
    time = 0
    eat = 0
    eat_flag = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append(start)
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < n and 0<= nc < n and  not matrix[nr][nc] > shark and eat_flag[nr][nc] != 1:
                # shark 보다 작으면 먹어야지
                if matrix[nr][nc] != 0 and matrix[nr][nc] < shark:
                    matrix[nr][nc] = 0
                    eat_flag[nr][nc] = 1
                # shark랑 같으면 먹지는 못해
                if matrix[nr][nc] == shark:
                    pass




n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

# 아기상어크기 -> 2 위치 -> 9
# 자신의 크기와 같은수의 먹을 때 마다 크기가 1 증가가
shark = 2
start = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            start.append(i)
            start.append(j)


exp = 0
cnt = 0
while True:
    r,c = start[0],start[1]
    dr,dc,dist = bfs(r,c)
    if dr == -1:
        break
    matri





