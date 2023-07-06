'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
from collections import deque

n,m,start = map(int,input().split(' '))
nodes = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split(' '))
    nodes[a][b] = nodes[b][a] = 1


dfs_visited = [0]*(n+1)

def dfs(start):

    dfs_visited[start] = 1

    print(start , end=' ')
    
    for i in range(n+1):
        if dfs_visited[i] == 0:
            if nodes[start][i] == 1:
                dfs(i)
            

dfs(start)
print()


bfs_visited = [0] * (n+1)

def bfs(start):
    queue = deque()
    queue.append(start)

    bfs_visited[start] = 1

    while queue:


        number = queue.popleft()

        print(number, end = ' ')

        for i in range(n+1):
            if bfs_visited[i] == 0:
                if nodes[number][i] == 1:
                    queue.append(i)
                    bfs_visited[i] = 1
        
        

bfs(start)
