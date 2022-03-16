import sys

sys.stdin = open('input.txt')
from collections import deque


# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c,idx):
    queue = deque()
    queue.append((r,c))
    nodes[r][c] = 1
    while queue:
        row,col = queue.popleft()
        for i in range(4):
            new_r = row + dr[i]
            new_c = col + dc[i]
            if 0 <= new_r < n and 0 <= new_c < n:
                if matrix[new_r][new_c] == 1 and nodes[new_r][new_c] == 0:
                    queue.append((new_r,new_c))
                    nodes[new_r][new_c] = 1
                    apt_list[idx] += 1


n = int(input())
matrix = [list(map(int,input())) for _ in range(n)]
nodes = [[0]*(n) for _ in range(n)]

apt_list={}
idx = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0 and nodes[i][j] == 0:
            apt_list[idx] = 1
            bfs(i,j,idx)
            idx+=1

apt_list = sorted(apt_list.values())
print(len(apt_list))
for i in apt_list:
    print(i)