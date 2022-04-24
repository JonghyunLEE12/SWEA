# 컴퓨터의 수
n = int(input())
m = int(input())

node = [[0]* (n+1) for i in range(n+1)]
stack = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    node[a][b] = node[b][a] = 1

rlt = []

def dfs(v):
    stack[v] = 1
    for i in range(1,n+1):
        if stack[i] == 0 and node[i][v] == 1:
            rlt.append(i)
            dfs(i)

dfs(1)
print(len(rlt))