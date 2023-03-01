n = int(input())
arr_n = sorted(list(map(int,input().split(' '))))
m = int(input())
arr_m = list(map(int,input().split(' ')))


def Binary(num,arr_n,start,end):

    if start > end:
        return 0

    mid = (start + end) // 2

    if num == arr_n[mid]:
        return 1

    elif num < arr_n[mid]:
        return Binary(num,arr_n,start,mid-1)
    else:
        return Binary(num,arr_n,mid+1,end)


for num in arr_m:
    start = 0
    end = n - 1
    print(Binary(num,arr_n,start,end))