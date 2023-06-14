'''
7
35
'''

n = int(input())
target = int(input())

matrix = [[0] * n for _ in range(n)]
visited = []

for mat in matrix:
    visited.append(mat[::])

# 델타 하 우 상 좌
dr = [1,0,-1,0]
dc = [0,1,0,-1]


direction = 0

row = 0
col = 0
number = n*n



while True:
    if number == 0:
        break

    matrix[row][col] = number

    if number == target:
        ans = [row+1,col+1]
    
    nr = row + dr[direction]
    nc = col + dc[direction]

    if nr < 0 or nc < 0 or nr >= n or nc >= n or matrix[nr][nc] != 0:
        direction = (direction + 1) % 4

    row = row + dr[direction]
    col = col + dc[direction]

    number -= 1


for mat in matrix:
    print(*mat)

print(*ans)