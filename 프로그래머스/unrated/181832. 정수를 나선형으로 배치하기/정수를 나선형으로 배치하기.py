from collections import deque
def solution(n):
    answer = [[]]
    
    # 델타 : 우 하 좌 상
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    move_list = [[0]*n for _ in range(n)]
    
    start_r, start_c = 0,0
    
    def endCheck():
        for i in range(n):
            for j in range(n):
                if move_list[i][j] == 0:
                    return False
        return True
    
    def bfs(r,c):
        move_direction = 0
        queue = deque()
        queue.append([r,c])
        move_list[r][c] = 1
        
        while queue:
            if endCheck():
                break
            row,col = queue.popleft()
            nr = row + dr[move_direction]
            nc = col + dc[move_direction]
            if 0 <= nr < n and 0 <= nc < n:
                if move_list[nr][nc] == 0:
                    queue.append([nr,nc])
                    move_list[nr][nc] += move_list[row][col] + 1
                else:
                    move_direction = (move_direction + 1) % 4
                    queue.append([row,col])
            else:
                move_direction = (move_direction + 1) % 4
                queue.append([row,col])
        return move_list
    
    return bfs(start_r,start_c)