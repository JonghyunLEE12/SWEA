# visited = []
# answer = 0

# def dfs(k):
#     global visited
#     if visited[k] == 1:
#         return
#     else:
#         for i in range(4):
#             dfs(i)
#     return 

# def solution(land):
#     global answer, visited
#     visited = [0] * len(land[0])
#     for i in range(len(land[0])):
#         visited[i] = 1
#         for j in range(len(land[0])):
#             dfs(j)
#         visited[i] = 0

#     return answer

def solution(land):
    answer = 0
    for i in range(1,len(land)):
        for j in range(4):
        	#같은 열을 지날 수 없으므로
            land[i][j]=max(land[i-1][:j]+land[i-1][j+1:])+land[i][j]
    return max(land[-1])