# def solution(n,computers):
#     answer = 0
#     parents = [ i for i in range(n) ]
    
#     def find(target):
#         if target == parents[target]:
#             return target
#         else:
#             y = find(parents[target])
#             parents[target] = y
#             return y
    
    
#     def union(a,b):
#         a = find(a)
#         b = find(b)
        
#         if a != b:
#             parents[a] = b
    
#     for i in range(len(computers)):
#         for j in range(len(computers[0])):
#             if computers[i][j] == 1:
#                 union(i,j)
    
    
#     network = set()
#     for i in range(n):
#         network.add(find(i))
        
#     answer = len(network)
#     return answer













# from collections import deque

# def bfs(start,computers,visited,n):
#     visited[start] = 1
#     queue = deque([start])
#     while queue:
#         v = queue.popleft()
#         for i in range(n):
#             if computers[v][i] and visited[i] == 0:
#                 visited[i] = 1
#                 queue.append((i))

# def solution(n,computers):
#     answer = 0
#     visited = [0] * n
#     for i in range(n):
#         if visited[i] == 0:
#             bfs(i,computers,visited,n)
#             answer += 1
#     return answer

def solution(n,computers):
    answer = 0
    parents = [ x for x in range(n)]
    
    def find(target):
        if parents[target] == target:
            return target
        else:
            y = find(parents[target])
            parents[target] = y
            return y
    
    def union(a,b):
        a = find(a)
        b = find(b)
        
        if a != b:
            parents[a] = b
    
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                union(i,j)
    
    
    network = set()
    
    for i in parents:
        network.add(find(i))
    

    return len(network)












