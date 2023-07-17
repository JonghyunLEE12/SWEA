'''
3
4
7
10
'''

t = int(input())


def dfs(value,total):
    global count
    if total >= n:
        return
    total += value

    if total == n:
        count +=1

    
    dfs(1,total)
    dfs(2,total)
    dfs(3,total)

for i in range(t):
    n = int(input())
    count = 0
    dfs(0,0)
    print(count)