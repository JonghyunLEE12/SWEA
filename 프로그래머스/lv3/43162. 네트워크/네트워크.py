# from collections import deque


# def bfs(start,computers,visited,n):
#     visited[start] = 1
#     queue = deque([start])
#     # queue.append([start])
#     while queue:
#         v = queue.popleft()
#         for i in range(n):
#             if computers[v][i] and visited[i] == 0:
#                 visited[i] = 1
#                 queue.append(i)

# def solution(n,computers):
#     answer = 0
#     visited = [0] * n
#     for i in range(n):
#         if visited[i] == 0:
#             bfs(i,computers,visited,n)
#             answer += 1
#     return answer













from collections import deque

def bfs(start,computers,visited,n):
    visited[start] = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in range(n):
            if computers[v][i] and visited[i] == 0:
                visited[i] = 1
                queue.append((i))

def solution(n,computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            bfs(i,computers,visited,n)
            answer += 1
    return answer