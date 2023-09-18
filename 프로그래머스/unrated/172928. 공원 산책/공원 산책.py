def solution(park, routes):
    answer = []
    
    for r in range(len(park)):
        for c in range(len(park[0])):
            if park[r][c] == 'S':
                start_r,start_c = r,c
                copy_r,copy_c = r,c
    
    # 델타 상 하 좌 우
    # 델타 북 남 서 동
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    def check(nr,nc):
        if 0 <= nr < len(park) and 0 <= nc <len(park[0]):
            if park[nr][nc] != 'X':
                return True
            else:
                return False
            
        return False
            
    
    print(start_r,start_c)
    for route in routes:
        flag = 0
        route = route.split(' ')
        
        if route[0] == 'N':
            for i in range(int(route[1])):
                nr = start_r + dr[0]
                nc = start_c + dc[0]
                
                if check(nr,nc):
                    start_r,start_c = nr,nc
                else:
                    flag += 1
                
        if route[0] == 'S':
            for i in range(int(route[1])):
                nr = start_r + dr[1]
                nc = start_c + dc[1]
                
                if check(nr,nc):
                    start_r,start_c = nr,nc
                else:
                    flag += 1
                    
        if route[0] == 'W':
            for i in range(int(route[1])):
                nr = start_r + dr[2]
                nc = start_c + dc[2]
                
                if check(nr,nc):
                    start_r,start_c = nr,nc
                else:
                    flag += 1
                    
        if route[0] == 'E':
            for i in range(int(route[1])):
                nr = start_r + dr[3]
                nc = start_c + dc[3]
                
                if check(nr,nc):
                    start_r,start_c = nr,nc
                else:
                    flag += 1
        
        if flag >= 1:
            start_r,start_c = copy_r,copy_c
        else:
            copy_r,copy_c = start_r,start_c
        
    

    return [start_r,start_c]