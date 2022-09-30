#델타 하 좌 우
dr = [1,0,1]
dc = [0,1,1]

def change_num(matrix,visited,row,col):
    visited[row][col] = 1
    for i in range(len(dr)):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < len(matrix) and 0 <= nc <len(matrix):
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                matrix[nr][nc] = matrix[row][col] + 1
    return matrix , visited

def make_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    visited = [[0]*len(matrix) for _ in range(len(matrix))]
    
    matrix[0][0] = 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                change_num(matrix,visited,i,j)
    return matrix

# def solution(n, left, right):
#     answer = []
#     matrix = make_matrix(n)
#     lst = []
#     for ma in matrix:
#         for m in ma:
#             lst.append(m)
#     answer = lst[left:right+1]
#     return answer


def solution(n,left,right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i%n , i//n)+1)
    return answer