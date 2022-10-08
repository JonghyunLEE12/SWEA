
T = int(input())
for tc in range(T):
    n = int(input())
    matrix = [list(map(int,input().split(' '))) for _ in range(2)]

    for j in range(1,n):
        if j == 1:
            # 대각선 의 값을 덯해 주는 과정
            matrix[0][j] += matrix[1][j-1]
            matrix[1][j] += matrix[0][j-1]
        else:
            matrix[0][j] += max(matrix[1][j-1] , matrix[1][j-2])
            matrix[1][j] += max(matrix[0][j-1], matrix[0][j-2])
    print(max(matrix[0][n-1], matrix[1][n-1]))