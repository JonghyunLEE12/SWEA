n = int(input())
arr = list(map(int,input().split()))


def dfs(depth):
    if depth == n:
        rlt.append( sum( abs(explore[i] - explore[i+1]) for i in range(n-1)))
        return
    for i in range(n):
        if visited[i]:
            continue
        explore.append(arr[i])
        visited[i] = 1
        dfs(depth+1)
        visited[i] = 0
        explore.pop()


visited = [0] * n
rlt,explore = [] , []
dfs(0)

print(max(rlt))
