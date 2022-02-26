import sys

sys.stdin = open('input.txt')

T = int(input())

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def delta(arr):
    p = 2
    sum_lst = []
    for r in range(len(arr)):
        for c in range(len(arr)):
            sum_num = arr[r][c]
            for i in range(1,p+1):
                for k in range(len(dr)):
                    new_r = r + dr[k]*i
                    new_c = c + dc[k]*i

                    if new_r < 0 or new_c < 0 or new_r >= N or new_c >=N:
                        break
                    else:
                        sum_num += arr[new_r][new_c]
            sum_lst.append(sum_num)

    max_sum = max(sum_lst)
    print(sum_lst)
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

