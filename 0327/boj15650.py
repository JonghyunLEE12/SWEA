'''
4 2
'''
'''
1 2
1 3
1 4
2 3
2 4
3 4
'''
def dfs(start):
    if len(stack) == m:
        print(*stack)
        return
    for i in range(start,n+1):
        stack.append(i)
        dfs(i+1)
        stack.pop()


n,m = list(map(int,input().split()))
stack = []
dfs(1)


