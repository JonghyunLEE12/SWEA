import sys

sys.stdin = open('input.txt')

'''
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.
'''

n,m,v = map(int,input().split())
nodes = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    nodes[a][b] = nodes[b][a] = 1

dfs_stack=[0]*(n+1)
def dfs(v):
    dfs_stack[v] = 1
    print(v,end=' ')
    for i in range(n+1):
        if dfs_stack[i] == 0 and nodes[i][v]:
            dfs(i)
dfs(v)

bfs_stack = [0]*(n+1)
from collections import deque
def bfs(v):
    bfs_stack[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        x = queue.popleft()
        print(x,end=' ')
        for i in range(n+1):
            if bfs_stack[i] == 0 and nodes[i][x]:
                queue.append(i)
                bfs_stack[i]=1
print()
bfs(v)