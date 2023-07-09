'''
5 3
...
.X.
.X.
.X.
...
'''

r,c = map(int,input().split(' '))
matrix = [list(map(str,input().rstrip(' '))) for _ in range(r)]

copy = [ mat[:] for mat in matrix ]


# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for row in range(r):
    for col in range(c):
        cnt = 0
        if matrix[row][col] == '.': continue

        for i in range(len(dr)):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < r and 0 <= nc < c:
                if matrix[nr][nc] == '.' :
                    cnt += 1
            else:
                cnt += 1

        if cnt >= 3:
            copy[row][col] = '.'




row_lst = []
col_lst = []

rlt_dict = { ".": "." , "X" : "X" }

for i in range(r):
    for j in range(c):
        if copy[i][j] == 'X':
            row_lst.append(i)
            col_lst.append(j)


if row_lst:
    row_l = min(row_lst)
    row_h = max(row_lst)
    col_l = min(col_lst)
    col_h = max(col_lst)

    for i in range(row_l,row_h+1):
        for j in range(col_l,col_h+1):
            print(rlt_dict[copy[i][j]],end = '')

        
        print()

else:
    print('X')
