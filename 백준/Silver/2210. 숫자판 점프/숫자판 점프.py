'''
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1
'''



matrix = [ list(map(int,input().split(' '))) for _ in range(5)]
result = []

# 델타 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]


# def dfs(row,col,number):
#     # number += str(matrix[row][col])
#     number += str(matrix[row][col])


#     if len(number) == 6:
#         if number not in result:
#             result.append(number)
#         return
    
#     for k in range(len(dr)):
#         nr = row + dr[k]
#         nc = col + dc[k]

#         if 0 <= nc < 5 and 0 <= nc < 5:
#             dfs(nr,nc,number)



# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(row, col, number):
    number += str(matrix[row][col])

    if len(number) == 6:
        if number not in result:
            result.append(number)
        return
    

    # 좌/우/위/아래 방향의 좌표를 탐색
    for i in range(len(dr)):
        nr = row + dr[i]
        nc = col + dc[i]

        # 맵 정보를 넘지 않는다면 탐색
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr,nc, number)

for i in range(5):
    for j in range(5):
        dfs(i,j,'')


print(len(result))