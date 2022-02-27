import sys

sys.stdin = open('input.txt')

T = int(input())

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def delta(arr):
    sum_lst = []
    for r in range(len(arr)):
        for c in range(len(arr)):
            p = arr[r][c]                # 중요
            sum_num = arr[r][c]
            for i in range(1,p):
                for k in range(len(dr)):
                    new_r = r + dr[k]*i
                    new_c = c + dc[k]*i
                    if 0 <= new_r < N and 0<= new_c < N:
                        sum_num += arr[new_r][new_c]
            sum_lst.append(sum_num)

    max_sum = 0
    for num in sum_lst:
        if num > max_sum:
            max_sum = num
    return max_sum

def three(arr):
    L = len(arr)
    sum_lst = []
    for i in range(L-3+1):
        for j in range(L-3+1):
            sum_num = 0
            for r in range(3):
                for c in range(3):
                    sum_num += arr[r+i][c+j]
            sum_lst.append(sum_num)
    max_sum = 0
    for k in sum_lst:
        if k > max_sum:
            max_sum = k
    return max_sum

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    ans1=three(matrix)
    ans2=delta(matrix)
    if ans1 > ans2:
        ans = ans1
    else:
        ans= ans2
    print(f'#{tc} {ans}')

