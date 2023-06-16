from collections import deque

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]
        for i in range(4):
            x = a + dr[i]
            y = b + dc[i]
            if 0 <= x < n and 0 <= y < m:
                if matrix[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x, y, 0])
                elif matrix[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x, y, w])
    return -1



n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, list(input().strip()))))
print(bfs())