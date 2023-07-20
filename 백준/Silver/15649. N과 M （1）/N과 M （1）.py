'''
4 2
'''

n,m = map(int,input().split(' '))

numbers = [x for x in range(1,n+1)]
visited = [0]*n

def dfs(arr):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(n):
        if visited[i] == 0:
            arr.append(numbers[i])
            visited[i] = 1
            dfs(arr)
            visited[i] = 0
            arr.pop()

for i in range(n):
    if visited[i] == 0:
        arr = [numbers[i]]
        visited[i] = 1
        dfs(arr)
        visited[i] = 0
        arr.pop()