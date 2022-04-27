import heapq

# 델타 : 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(row,col):
    queue = []
    heapq.heappush(queue,(0,0,row,col))
    while queue:
        count_g,count_gr,r,c = heapq.heappop(queue)
        # 꽃을 만나면 return
        if matrix[r][c] == 'F':
            print(count_g,count_gr)
            return
        for ii in range(4):
            nr = r + dr[ii]
            nc = c + dc[ii]
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == 0:
                    # 쓰레기 주변 count
                    if matrix[nr][nc] == 'gr':
                        heapq.heappush(queue,(count_g,count_gr+1,nr,nc))
                    # 쓰레기 일때 count
                    elif matrix[nr][nc] == 'g':
                        heapq.heappush(queue,(count_g+1,count_gr,nr,nc))
                    # 일반 길 일때는 no count
                    else:
                        heapq.heappush(queue,(count_g,count_gr,nr,nc))
                    visited[nr][nc] = 1

#  row = > m, col = > n
n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
start_r,start_c = 0,0


# 쓰레기 주변 표시 해주자
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'g':
            for k in range(4):
                new_r = i + dr[k]
                new_c = j + dc[k]
                if 0 <= new_r < n and 0 <= new_c < m and matrix[new_r][new_c] == '.':
                    matrix[new_r][new_c] = 'gr'
        # 하는 김에 start 지점도
        if matrix[i][j] == 'S':
            start_r = i
            start_c = j

bfs(start_r,start_c)
