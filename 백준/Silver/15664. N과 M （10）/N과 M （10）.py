'''
4 2
9 7 9 1
'''

n,m = map(int,input().split(' '))
nums = list(map(int,input().split(' ')))
nums.sort()
visited = [0]*n


rlt = set()

def dfs(arr):
    if len(arr) == m:
        rlt.add(tuple(arr))
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(nums[i])
            dfs(arr)
            arr.pop()
            visited[i] = 0


for i in range(n):
    if visited[i] == 0:
        visited[i] = 1
        arr = [ nums[i] ]
        dfs(arr)
        arr.pop()
        visited[i] = 1


result = [ a for a in rlt ]
result.sort()


def check(ans):
    if len(ans) == 1:
        return True
    
    for i in range(len(ans)-1):
        for j in range(i,len(ans)):
            if ans[i] > ans[j]:
                return False
    return True
    
for ans in rlt:
    if check(ans):
        print(*ans)