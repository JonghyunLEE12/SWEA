n,m = map(int,input().split(' '))
visited = [0]*n
rlt = []

def dfs():
    if len(rlt) == m:
        print(*rlt)
        return
    
    for i in range(1,n+1):
        if i not in rlt:
            rlt.append(i)
            dfs()
            rlt.pop()

dfs()