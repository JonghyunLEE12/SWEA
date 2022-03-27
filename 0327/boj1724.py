'''
6 5
1 2
2 5
5 1
3 4
4 6
'''

def dfs(i):
    visited[i] = 1
    for k in range(1,n+1):
        if nodes[i][k] == 1 and visited[k] == 0:
            dfs(k)

n,m = map(int,input().split())
nodes = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    nodes[a][b] = nodes[b][a] = 1
cnt = 0

for i in range(1,n+1):
    if visited[i] ==0:
        dfs(i)
        cnt += 1

print(cnt)