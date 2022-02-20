import sys

sys.stdin = open('input.txt')

T = 10

def rlt(col):
    row = 99

    # 델타
    # 좌, 우, 상
    dr = [0,0,-1]
    dc = [-1,1,0]
    direction = 0
    while True:
        if row <= 0:
            break
        new_r = row + dr[direction]
        new_c = col + dc[direction]
        if 0 <= new_r < 100 and 0<= new_c <100:
            if matrix[new_r][new_c] == 1:
                row = new_r
                col = new_c
                matrix[new_r][new_c] = 0
        direction = (direction+1) % 3
    return col
def find_2(arr):
    row = 99
    for i in range(100):
        if arr[row][i] == 2:
            col = i
    return col

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]
    ans = rlt(find_2(matrix))
    print(f'#{tc} {ans}')

