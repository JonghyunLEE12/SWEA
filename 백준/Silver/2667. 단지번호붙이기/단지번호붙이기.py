from collections import deque

# 델타 : 상하좌우

dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 방문처리도 있으면 좋을듯
def bfs(row,col,apt_num):
    queue = deque()
    queue.append((row,col))
    visited[row][col] = 1
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위체크 한번 해주자
            if 0 <= nr < n and 0<= nc < n:
                if matrix[nr][nc] != 0 and visited[nr][nc] == 0:
                    apt_list[apt_num] += 1
                    queue.append((nr,nc))
                    visited[nr][nc] = 1

n = int(input())
matrix = [ list(map(int,input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]


apt_num = 0
apt_list = dict()
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0 and visited[i][j] == 0:
            apt_list[apt_num] = 1
            bfs(i,j,apt_num)
            apt_num += 1

apt_list = sorted(apt_list.values())
print(len(apt_list))
for i in apt_list:
    print(i)


