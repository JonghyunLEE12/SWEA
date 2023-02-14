# from collections import deque


# def solution(x, y, n):
#     def bfs(x, y, n):
#         q = deque()
#         dist[x] = 1
#         q.append(x)

#         while q:
#             x = q.popleft()
#             if 0 <= x + n <= 1000000 and dist[x + n] == 0:
#                 dist[x + n] = dist[x] + 1
#                 q.append(x + n)
#             if 0 <= x * 2 <= 1000000 and dist[x * 2] == 0:
#                 dist[x * 2] = dist[x] + 1
#                 q.append(x * 2)
#             if 0 <= x * 3 <= 1000000 and dist[x * 3] == 0:
#                 dist[x * 3] = dist[x] + 1
#                 q.append(x * 3)

#     dist = [0] * 1000001
#     bfs(x,y,n)

#     return dist[y]-1


from collections import deque

def solution(x,y,n):
    
    dist = [0]*1000001
    def bfs(x,y,n):
        queue = deque()
        dist[x] = 1
        queue.append(x)
        
        while queue:
            nx = queue.popleft()
            
            if 0 <= nx+n <= 1000000 and dist[nx+n] == 0:
                dist[nx+n] = dist[nx] + 1
                queue.append(nx+n)
            
            if 0 <= nx*2 <= 1000000 and dist[nx*2] == 0:
                dist[nx*2] = dist[nx] + 1
                queue.append(nx*2)
                
            if 0 <= nx*3 <= 1000000 and dist[nx*3] == 0:
                dist[nx*3] = dist[nx] + 1
                queue.append(nx*3)
    
    bfs(x,y,n)
    
    answer = dist[y]-1
    return answer