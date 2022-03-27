# 푸는중
N , M = map(int,input().split())
maze = []
for i in range(M):
    maze.append(input())

cnt = 0

# R의 위치값을 찾는다
for i in range(len(maze)):
    for j in range(len(maze)):
        if maze[i][j] == 'R':
            r_x = i
            r_y = j

# B의 위치 값
for i in range(len(maze)):
    for j in range(len(maze)):
        if maze[i][j] == 'B':
            b_x = i
            b_y = j

print(f'R : {(r_x,r_y)}')
print(f'B : {(b_x,b_y)}')


