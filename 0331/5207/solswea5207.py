import sys

sys.stdin = open('input.txt')

T = int(input())

def binary_search(arr,target):
    global cnt
    left = 0
    right = n - 1

    flag = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            cnt += 1
            return
        elif arr[mid] > target:
            if flag == 0:
                break
            right = mid - 1
            flag = 0
        else:
            if flag == 1:
                break
            left = mid + 1
            flag = 1


for tc in range(1, T + 1):
    n,m = map(int,input().split())
    nums = sorted(list(map(int,input().split())))
    find_nums = list(map(int,input().split()))
    cnt = 0
    for i in find_nums:
        binary_search(nums,i)
    print(f'#{tc} {cnt}')

