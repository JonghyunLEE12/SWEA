'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
def dfs(v):
    stack[v] = 1
    for i in range(computers+1):
        if stack[i] == 0 and nodes[i][v]:
            rlt.append(i)
            dfs(i)

computers = int(input())
m = int(input())

nodes = [[0]*(computers+1) for _ in range(computers+1)]
stack = [0]*(computers+1)

for i in range(m):
    a,b = map(int,input().split())
    nodes[a][b] = nodes[b][a] = 1


rlt = []
dfs(1)
print(len(rlt))
