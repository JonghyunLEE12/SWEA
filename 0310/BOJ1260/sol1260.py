import sys

sys.stdin = open('input.txt')

from collections import deque


def dfs(V):
    stack_dfs[V] = 1
    rlt1.append(V)
    for i in range(N+1):
        if stack_dfs[i] == 0 and node[i][V]:
            dfs(i)


def bfs(v):
    stack_bfs[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        n = queue.popleft()
        rlt2.append(n)
        for i in range(N+1):
            if stack_bfs[i] == 0 and node[i][n]:
                queue.append(i)
                stack_bfs[i] = 1


# 정점의 개수 N , 간선의 개수 M , 탐색을 시작할 정점의 번호 V
N,M,V = map(int,input().split())
node = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    node[a][b] = node[b][a] = 1         # 노드의 연결상태 확인 가능
print(node)
stack_dfs = [0] * (N+1)
rlt1=[]
dfs(V)
print(*rlt1)
rlt2=[]
stack_bfs = [0] * (N+1)
bfs(V)
print(*rlt2)