import sys
from copy import deepcopy

sys.stdin = open('input.txt')

T = 10
def column(arr):
    # 시작 점 구하기
    col_list = []
    for i in range(100):
        if arr[0][i] == 1:
            col_list.append(i)
    return col_list

def count_ladder(arr):
    col_list=column(arr)

    # 델타
    # 좌, 우, 하
    dr = [0, 0, 1]
    dc = [-1, 1, 0]

    cnt_list = []                 # 이동거리 구하기

    for i in range(len(col_list)):
        copy_arr = deepcopy(arr)
        r = 0
        c = col_list[i]
        direction = 0
        cnt = 0
        while True:
            if r >= 99:
                break
            new_r = r + dr[direction]
            new_c = c + dc[direction]

            if 0 <= new_r < 100 and 0 <= new_c < 100:
                if copy_arr[new_r][new_c] == 1:
                    cnt += 1
                    r = new_r
                    c = new_c
                    copy_arr[new_r][new_c] = 0
            direction = (direction+1)%3
        cnt_list.append(cnt)
    return col_list,cnt_list

def find_min(col_list,cnt_list):
    min_num = cnt_list[0]
    idx = 0
    rlt_idx = 0
    for i in cnt_list:
        if i < min_num:
            rlt_idx = idx
            min_num = i
        idx += 1
    return col_list[rlt_idx]


for tc in range(1, T + 1):
    N = int(input())
    ladders = [list(map(int,input().split())) for _ in range(100)]
    rlt = count_ladder(ladders)
    col_list,cnt_list=rlt
    print(f'#{tc} {find_min(col_list,cnt_list)}')

