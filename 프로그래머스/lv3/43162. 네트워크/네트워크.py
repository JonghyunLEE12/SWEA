from collections import deque
def bfs(start, visited, computers,n):
    visited[start] = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in range(n):
            # 방문하지 않은 연결된 컴퓨터
            if computers[v][i] == 1 and not visited[i]:
                visited[i] = 1
                queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    for i in range(n):
        if visited[i] == 0:
            bfs(i,visited,computers,n)
            answer += 1
    return answer