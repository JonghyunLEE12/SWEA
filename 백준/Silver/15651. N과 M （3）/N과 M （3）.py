n,m = map(int,input().split(' '))
visited = [0]*(n+1)


comb = []


def dfs(comb,start):
    if len(comb) == m:
        print(*comb)
        return
    
    for i in range(1,n+1):
        comb.append(i)
        dfs(comb,i+1)
        comb.pop()


for i in range(1,n+1):
    comb.append(i)
    dfs(comb,i)
    comb.pop()