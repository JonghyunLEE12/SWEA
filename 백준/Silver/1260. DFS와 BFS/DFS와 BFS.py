n,m,v = map(int,input().split())
nodes = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    nodes[a][b] = nodes[b][a] = 1


dfs_stack = [0] * (n+1)
def dfs(v):
    dfs_stack[v] = 1
    print(v,end=' ')
    for i in range(n+1):
        if dfs_stack[i] == 0 and nodes[i][v] == 1:
            dfs(i)
dfs(v)


from collections import deque
bfs_stack = [0] * (n+1)

def bfs(v):
    bfs_stack[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        a = queue.popleft()
        print(a,end=' ')
        for i in range(n+1):
            if bfs_stack[i] == 0 and nodes[i][a]:
                queue.append(i)
                bfs_stack[i] = 1
print()
bfs(v)
