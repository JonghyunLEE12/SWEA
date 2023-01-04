from collections import deque

def solution(maps):
    answer = 0
    
    # 델타 상 하 좌 우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    def bfs(r,c):
        count = 0
        flag = False
        queue = deque()
        queue.append((r,c))
        visited[r][c] = 9
        while queue:
            row,col = queue.popleft()
            for i in range(len(dr)):
                nr = row + dr[i]
                nc = col + dc[i]
                
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]):
                    if visited[nr][nc] == 0 and maps[nr][nc] != 0:
                        if (nr,nc) == (len(maps)-1,len(maps[0])-1):
                            flag = True
                        visited[nr][nc] = 9
                        maps[nr][nc] += maps[row][col]
                        queue.append((nr,nc))
        return flag
    
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    start_r,start_c = 0,0
    end_r,end_c = 0,0
    
    rlt = bfs(start_r,start_c)

    if rlt == True:
        answer = maps[-1][-1]
    else :
        answer = -1

    
    return answer