from collections import deque

# n,m = map(int,input().split(' '))
# matrix = [ list(input()) for _ in range(n)]
# visited = [[0]*m for _ in range(n)]

# start_r, start_c = 0,0

# # 델타 상 하 좌 우
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]


# for r in range(n):
#     for c in range(m):
#         if matrix[r][c] == '0':
#             start_r,start_c = r,c


# keyDict = {}
# for i in range(6):
#     keyDict[chr(i+65)] = 0

# lowerKey = [ x.lower() for x in keyDict.keys() ]


# def bfs(r,c):
#     queue = deque()
#     queue.append([r,c])
#     visited[r][c] = 1

#     while queue:
#         row,col = queue.popleft()
#         for i in range(len(dr)):
#             nr = row + dr[i]
#             nc = col + dc[i]

#             if 0 <= nr < n and 0 <= nc < m:
#                 # if matrix[nr][nc] != '#':
#                 if visited[nr][nc] == 0 and matrix[nr][nc] != '#':
#                     if matrix[nr][nc] in keyDict.keys():
#                         if keyDict[matrix[nr][nc]] == 0: continue
#                         else:
#                             keyDict[matrix[nr][nc]] -= 1
#                             queue.append([nr,nc])
#                             visited[nr][nc] += visited[row][col]
#                             continue
#                     elif matrix[nr][nc] in lowerKey:
#                         keyDict[matrix[nr][nc].upper()] += 1
#                         queue.append([nr,nc])
#                         visited[nr][nc] += visited[row][col]
#                         continue
                    
#                     if matrix[nr][nc] == '1':
#                         visited[nr][nc] += visited[row][col]
#                         return visited[nr][nc]
#                     queue.append([nr,nc])
#                     visited[nr][nc] += visited[row][col]
                    



# print(bfs(start_r,start_c))



n, m = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
dx = -1, 0, 1, 0
dy = 0, 1, 0, -1
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == "0":
            graph[i][j] = "."
            q.append((i, j, 0))
            break

while q:
    x, y, key = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nkey = key
        # 범위 안 이면서 벽도 아니고 동일한 키를 가지고 그곳에 방문한 적이 없어야 한다.
        if (
            0 <= nx < n
            and 0 <= ny < m
            and graph[nx][ny] != "#"
            and visited[nx][ny][key] == 0
        ):
            # 문인 경우
            # 열쇠가 없으면 continue
            # & 연산으로 1 혹은 0이 나오게 된다.
            if graph[nx][ny].isupper():
                if not (key & 1 << (ord(graph[nx][ny]) - ord("A"))):
                    continue
            # 열쇠인 경우
            # or 연산을 통해 key를 교체
            # a키만 가지고 c키를 먹는다면
            # 1 -> 101이 된다.
            elif graph[nx][ny].islower():
                nkey |= 1 << ord(graph[nx][ny]) - ord("a")
            elif graph[nx][ny] == "1":
                print(visited[x][y][key] + 1)
                exit()
            q.append((nx, ny, nkey))
            visited[nx][ny][nkey] = visited[x][y][key] + 1
print(-1)