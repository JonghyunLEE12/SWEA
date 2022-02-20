import sys

sys.stdin = open('input.txt')

T = int(input())

def sum_arr(arr):
    sum_lst = []
    for i in range(n-m+1):
        sum_num = 0
        for j in range(m):
            sum_num += arr[i+j]
        sum_lst.append(sum_num)
    return sum_lst

for tc in range(1, T + 1):
    n , m = map(int,input().split())
    arr = list(map(int,input().split()))
    sum_lst = sum_arr(arr)
    max_num = sum_lst[0]
    min_num = sum_lst[0]
    for i in sum_lst:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i
    rlt = max_num - min_num
    print(f'#{tc} {rlt}')

