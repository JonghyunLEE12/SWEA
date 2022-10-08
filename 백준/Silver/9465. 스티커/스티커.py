T = int(input())

for tc in range(T):
    n = int(input())
    matrix = [list(map(int,input().split(' '))) for _ in range(2)]

    for i in range(1,n):
        if i == 1:                                                      # i = 1 일 때, 대각전 0 열 의 수를 더해준다
            matrix[0][i] += matrix[1][i-1]
            matrix[1][i] += matrix[0][i-1]
        else:
            matrix[0][i] += max(matrix[1][i-1], matrix[1][i-2])         # 같은 변을 공유할 수는 없다, i-1 열 과 i-2열을 비교하여 최대값을 더해준다
            matrix[1][i] += max(matrix[0][i-1], matrix[0][i-2])

    
    print(max(matrix[0][n-1], matrix[1][n-1]))