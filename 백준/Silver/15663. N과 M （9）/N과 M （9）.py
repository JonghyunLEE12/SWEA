'''
4 2
9 7 9 1
'''

n,m = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))
arr.sort()
visited = [0]*n



rlt = set()
def dfs(lst):
    if len(lst) == m:
        rlt.add(tuple(lst))
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i]= 1
            lst.append(arr[i])
            dfs(lst)
            lst.pop()
            visited[i] = 0

for i in range(n):
    if visited[i] == 0:
        visited[i] = 1
        lst = [arr[i]]
        dfs(lst)
        lst.pop()
        visited[i] = 0


result = []

for a in rlt:
    result.append(a)


result.sort()

for ans in result:
    print(*ans)