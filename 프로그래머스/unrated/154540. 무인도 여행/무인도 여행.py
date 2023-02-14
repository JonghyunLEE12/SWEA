from collections import deque

def solution(maps):
    answer = []
    
    # 델타 상 하 좌 우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    
    sum_group = []
    
    def bfs(row,col,sum_num):
        queue = deque()
        queue.append([row,col])
        visited[row][col] = 1
        
        while queue:
            r,c = queue.popleft()
            for i in range(len(dr)):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]):
                    if maps[nr][nc] != 'X' and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        queue.append([nr,nc])
                        sum_num += int(maps[nr][nc])
        
        return sum_num
                        
                        
                
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] != 'X' and visited[r][c] == 0:
                sum_num = int(maps[r][c])
                sum_group.append(bfs(r,c,sum_num))
    
    if len(sum_group) == 0:
        return [-1]
    else:
        sum_group.sort()
        return sum_group
    