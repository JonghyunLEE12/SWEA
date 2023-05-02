import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(x, depth):
    visited[x] = True
    d[x] = depth
    for child in graph[x]:
        if visited[child]:  continue
        dfs(child, depth + 1)
        
t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    d = [0] * (n + 1)
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        parent[b] = a
    
    for i in range(1, n + 1):
        if parent[i] == 0:
            dfs(i, 0)
            break
    
    a, b = map(int, input().split())
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    print(a)