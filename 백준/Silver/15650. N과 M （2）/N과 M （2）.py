n,m = map(int,input().split(' '))
visited = [0]*(n+1)


def dfs(comb,start):
    if len(comb) == m:
        print(*comb)
        return
    
    for i in range(start,n+1):
        if visited[i] == 0:
            visited[i] = 1
            comb.append(i)
            dfs(comb,i+1)
            comb.pop()
            visited[i] = 0


comb = []
for i in range(1,n+1):
    if visited[i] == 0:
        visited[i] = 1
        comb.append(i)
        dfs(comb,i)
        comb.pop()
        visited[i] = 0