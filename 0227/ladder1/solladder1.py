import sys

sys.stdin = open('input.txt')

T = 10

# 델타 : 좌 우 상
dr = [0,0,-1]
dc = [-1,1,0]
def delta(arr,col):
    row = 99
    direction = 0
    while True:
        if row <= 0:
            break
        new_r = row + dr[direction]
        new_c = col + dc[direction]
        if 0<= new_r < 100 and 0<= new_c < 100:
            arr[row][col] = 0
            if arr[new_r][new_c] == 1:
                row = new_r
                col = new_c
        direction = (direction + 1) % 3

    return col

def find_2(arr):
    for i in range(len(arr)):
        if arr[99][i] == 2:
            col = i
    return col

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]
    col = find_2(matrix)
    ans = delta(matrix,col)
    print(f'#{tc} {ans}')

