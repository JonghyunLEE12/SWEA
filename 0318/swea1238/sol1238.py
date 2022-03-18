import sys

sys.stdin = open('input.txt')

from collections import deque

T = 10

def bfs(start):
    queue = deque()
    queue.append(start)
    stack[start] = 1
    while queue:
        start = queue.popleft()
        for next in range(1,N+1):
            if nodes[start][next] and not stack[next]:
                stack[next] = 1
                queue.append(next)
                distance[next] = distance[start] + 1


for tc in range(1, T + 1):
    length , start = map(int,input().split())
    matrix = list(map(int,input().split()))
    N = max(matrix)
    nodes = [[0]*(N+1) for _ in range(N+1)]

    for i in range(length//2):
        start = matrix[i*2]
        end = matrix[(i*2)+1]
        nodes[start][end] = 1

    stack = [0] * (N+1)
    distance = [0] * (N+1)

    bfs(start)

    max_num = distance[0]
    for i in range(1,len(distance)):
        if distance[i] >= max_num:
            max_num = distance[i]
            index = i
    
    print(f'#{tc} {index}')

