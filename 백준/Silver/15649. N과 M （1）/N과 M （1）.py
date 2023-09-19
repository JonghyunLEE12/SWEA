'''
4 2
'''

n,m = map(int,input().split(' '))
visited = [0]*(n+1)


def dfs(arr,start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1,n+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            dfs(arr,i)
            arr.pop()
            visited[i] = 0


for i in range(1,n+1):
    if visited[i] == 0:
        visited[i] = 1
        arr = [i]
        dfs(arr,i)
        arr.pop()
        visited[i] = 0