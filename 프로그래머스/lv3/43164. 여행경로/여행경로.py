# from collections import deque
# from pprint import pprint

# def solution(tickets):
#     answer = []
#     visited = [[0]* len(tickets)]
#     # print(visited)
    
    
#     def dfs(start,cnt):
#         if cnt == len(tickets)+1:
#             return
#         for i in range(start,len(tickets)):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 dfs(i,cnt+1)
#                 visited[i] = 0
        
#     for i in range(len(tickets)):
#         if tickets[i][0] == 'ICN' and visited[i] == 0:
#             visited[i] = 1
#             dfs(i,0)
#             visited[i] = 0
            
#     return answer

import collections
answer = []
graph = collections.defaultdict(list)
visited = collections.defaultdict(list)

def dfs(s, cnt, list, l):
    if cnt == l:
        answer.append(list)
        return
    
    if len(answer) >= 1:
        return

    for a in range(len(graph[s])):
        if visited[s][a] == 0:
            visited[s][a] = 1
            dfs(graph[s][a], cnt+1, list+[graph[s][a]], l)
            visited[s][a] = 0

def solution(tickets):
    
    for a,b in tickets:
        graph[a].append(b)
        visited[a].append(0)
    for a, b in graph.items():
        graph[a].sort()

    dfs("ICN",0, ["ICN"], len(tickets))

    return answer[:][0]