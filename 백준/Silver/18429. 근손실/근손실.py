n,k = map(int,input().split())
kit = list(map(int,input().split()))


def dfs(depth,t):
    global count
    if depth == n:
        count += 1
        return
    for i in range(n):
        if check[i] or t + kit[i]-k < 0:
            continue
        check[i] = 1
        dfs(depth+1, t+kit[i]-k)
        check[i] = 0

check = [0]*n
count = 0
dfs(0,0)
print(count)