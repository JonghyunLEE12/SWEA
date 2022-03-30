import sys

sys.stdin = open('input.txt')

T = int(input())

def partition(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_arr = partition(arr[:middle])
    right_arr = partition(arr[middle:])
    return merge(left_arr,right_arr)

def merge(left_lst, right_lst):
    global cnt
    left_N = len(left_lst)
    right_N = len(right_lst)
    result = [0]*(left_N+right_N)
    left_i, right_i = 0, 0
    i = 0
    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    while left_i < left_N or right_i < right_N:
        if left_i < left_N and right_i < right_N:
            if left_lst[left_i] <= right_lst[right_i]:
                result[i] = left_lst[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right_lst[right_i]
                i += 1
                right_i += 1

        elif left_i < left_N:
            result[i] = left_lst[left_i]
            i += 1
            left_i += 1
        elif right_i < right_N:
            result[i] = right_lst[right_i]
            i += 1
            right_i += 1
    return result



for tc in range(1, T + 1):
    n = int(input())
    matrix = list(map(int,input().split()))
    cnt = 0
    data = partition(matrix)
    print(f'#{tc} {data[n//2]} {cnt}')

