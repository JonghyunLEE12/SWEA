answer = 0
visited = []
n = 0

def solution(k, dungeons):
    global n , visited
    n = len(dungeons)
    visited = [0] * n
    dfs(k,0,dungeons)
    
    return answer

def dfs(k,count,dungeons):
    global answer
    if count > answer:
        answer = count
        
    for i in range(n):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k-dungeons[i][1] , count +1 , dungeons)
            visited[i] = 0


# answer = 0
# N = 0
# visited = []


# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:
#         answer = cnt

#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0


# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#     return answer