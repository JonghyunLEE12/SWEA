import sys

sys.stdin = open('input.txt')

from collections import deque

T = int(input())

def bfs(start_node):
    result = 0
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        start_node = queue.popleft()
        for next_node in range(1, v+1):
            if nodes[start_node][next_node] and not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1
                distance[next_node] = distance[start_node] +1
                if next_node == end:
                    result = distance[next_node]
                    return result
    return result

for tc in range(1, T + 1):
    v,e = map(int,input().split())
    nodes = [[0]*(v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    distance = [0] * (v+1)
    for i in range(e):
        a,b = map(int,input().split())
        nodes[a][b] = nodes[b][a] = 1

    start,end = map(int,input().split())
    
    print(f'#{tc} {bfs(start)}')

