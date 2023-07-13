def solution(board):
    answer = 0
    
    # 델타 상 하 좌 우 대 각 선
    dr = [-1,1,0,0,1,1,-1,-1]
    dc = [0,0,-1,1,1,-1,1,-1]
    
    visited = [[0]*len(board[0]) for _ in range(len(board))]
    
    def checking(r,c):
        
        visited[r][c] = 1
        
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
    
    for r in range(len(board)):
        for c in range(len(board[0])):          
            if board[r][c] == 1:
                checking(r,c)
    
    
    for vi in visited:
        cnt = vi.count(0)
        answer += cnt
                
    return answer