# def solution(dirs):
#     answer = 0
#     matrix = [ [0]*10 for _ in range(10)]
#     visited = [[0]*10 for _ in range(10)]
    
#     # 델타 상 하 좌 우
#     dr = [-1,1,0,0]
#     dc = [0,0,-1,1]
    
#     row , col = 5,5
#     for loca in dirs:
#         if loca == 'U':
#             nr = row + dr[0]
#             nc = col + dc[0]
#             if 0 <= nr < 10 and 0 <= nc < 10:
#                 if visited[nr][nc] == 0:
#                     # 처음 가보는길
#                     answer += 1
#                     row , col = nr , nc
#                 else:
#                      row,col = nr , nc
#             else:
#                 continue
#         elif loca == 'D':
#             nr = row + dr[1]
#             nc = col + dc[1]
#             if 0 <= nr < 10 and 0 <= nc < 10:
#                 if visited[nr][nc] == 0:
#                     # 처음 가보는길
#                     answer += 1
#                     row , col = nr , nc
#                 else:
#                      row,col = nr , nc
#             else:
#                 continue
#         elif loca == 'L':
#             nr = row + dr[2]
#             nc = col + dc[2]
#             if 0 <= nr < 10 and 0 <= nc < 10:
#                 if visited[nr][nc] == 0:
#                     # 처음 가보는길
#                     answer += 1
#                     row , col = nr , nc
#                 else:
#                      row,col = nr , nc
#             else:
#                 continue
#         elif loca == 'D':
#             nr = row + dr[3]
#             nc = col + dc[3]
#             if 0 <= nr < 10 and 0 <= nc < 10:
#                 if visited[nr][nc] == 0:
#                     # 처음 가보는길
#                     answer += 1
#                     row , col = nr , nc
#                 else:
#                      row,col = nr , nc
#             else:
#                 continue
    
#     return answer 


def solution(dirs):
    command = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    road = set()
    cur_x, cur_y = (0,0)
    
    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1]
        if -5<= next_x <=5 and -5<= next_y <=5:
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    return len(road) // 2