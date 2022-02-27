import sys
from copy import deepcopy
sys.stdin = open('input.txt')

T = 10

# 델타 좌, 우 , 아래
dr = [0,0,1]
dc = [-1,1,0]

def delta(arr):
    rlt_lst = []
    for r in range(1):
        for c in range(len(arr)):
            if arr[r][c] == 1:
                copy_arr = deepcopy(arr)
                now_c = c
                sum_cnt = 0
                direction = 0
                row = r
                col = c
                while True:
                    if row >= 99:
                        break
                    new_r = row + dr[direction]
                    new_c = col + dc[direction]
                    if 0 <= new_r < 100 and 0 <= new_c < 100:
                        if copy_arr[new_r][new_c] == 1:
                            copy_arr[row][col] = 0
                            row = new_r
                            col = new_c
                            sum_cnt += 1
                    direction = (direction + 1) % 3
                rlt_lst.append((sum_cnt,now_c))
    return rlt_lst

for tc in range(1, T + 1):
    N = int(input())
    # 100 x 100
    matrix = [ list(map(int,input().split())) for _ in range(100)]
    rlt_lst = delta(matrix)
    rlt_lst.sort()
    print(f'#{tc} {rlt_lst[0][1]}')

