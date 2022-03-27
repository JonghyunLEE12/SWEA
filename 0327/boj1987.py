'''
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
'''
# 10
import pprint

# 델타
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(x,y,count):
    global ans
    ans = max(ans,count)
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if 0 <= nr < r and 0 <= nc < c and not matrix[nr][nc] in alpha:
            alpha.add(matrix[nr][nc])
            dfs(nr, nc, count+1)
            alpha.remove(matrix[nr][nc])


r,c = map(int,input().split())
matrix = [list(input()) for _ in range(r)]
ans = 0
alpha = set()
alpha.add(matrix[0][0])
dfs(0,0,1)

print(ans)
