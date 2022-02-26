import sys

sys.stdin = open('input.txt')

T = int(input())

def delta(arr):
    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    L = len(arr)
    sum_lst=[]
    for r in range(L):
        for c in range(L):
            sum_num = arr[r][c]
            for k in range(4):
                new_r = r + dr[k] *2
                new_c = c + dc[k] *2
                if new_r < 0 or new_r >= L or new_c < 0 or new_c >= L:
                    break
                else:
                    sum_num += arr[new_r][new_c]
            sum_lst.append(sum_num)

    max_sum = sum_lst[0]
    for i in sum_lst:
        if i > max_sum:
            max_sum = i
    return max_sum

def three(arr):
    L = len(arr)
    sum_list = []
    for i in range(L-3+1):
        for j in range(L-3+1):
            sum_num = 0
            for a in range(3):
                for b in range(3):
                    sum_num += arr[i+a][j+b]
            sum_list.append(sum_num)
    if len(sum_list) == 0:
        return 0
    else:
        max_num = sum_list[0]
        for i in sum_list:
            if i > max_num:
                max_num = i
    return max_num

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    rlt_1 = delta(matrix)
    rlt_2 = three(matrix)
    if rlt_1 > rlt_2:
        ans = rlt_1
    else:
        ans = rlt_2
    print(f'#{tc} {ans}')

