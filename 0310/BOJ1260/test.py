import sys

sys.stdin = open('input.txt')

from collections import deque

n,m,v = map(int,input().split())
node = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    node[a][b] = node[b][a] = 1

stack_dfs=[0]*(n+1)
rlt1 = []
def dfs(v):
    stack_dfs[v] = 1
    rlt1.append(v)
    for i in range(n+1):
        if stack_dfs[i] == 0 and node[i][v]:
            dfs(i)
dfs(v)
print(*rlt1)

stack_bfs=[0]*(n+1)
rlt2 = []

def bfs(v):
    stack_bfs[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        num = queue.popleft()
        rlt2.append(num)
        for i in range(n+1):
            if stack_bfs[i] == 0 and node[i][num]:
                queue.append(i)
                stack_bfs[i] = 1

bfs(v)
print(*rlt2)