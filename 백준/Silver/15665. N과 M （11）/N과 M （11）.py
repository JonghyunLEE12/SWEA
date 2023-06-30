'''
4 2
9 7 9 1
'''


n,m = map(int,input().split(' '))
nums = list(map(int,input().split(' ')))
visited = [0]*n

nums.sort()


rlt = set()
def dfs(arr):

    if len(arr) == m:
        if tuple(arr) not in rlt:
            rlt.add(tuple(arr))
            print(*arr)
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 0
            arr.append(nums[i])
            dfs(arr)
            arr.pop()
            visited[i] = 0



for i in range(n):
    if visited[i] == 0:
        visited[i] = 0
        arr = [ nums[i] ]
        dfs(arr)
        arr.pop()
        visited[i] = 0