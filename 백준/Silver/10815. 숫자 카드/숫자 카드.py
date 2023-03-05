N = int(input())
arr_n = sorted(list(map(int,input().split(' '))))

M = int(input())
arr_m = list(map(int,input().split(' ')))

arr_n = list(set(arr_n))


rlt = []

def binary(N,target):
    start = 0
    end = len(N)-1

    while start <= end:
        if N[start] == target or N[end] == target:
            rlt.append(1)
            return
        mid = (start + end) // 2

        if N[mid] == target:
            rlt.append(1)
            return
        elif N[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    rlt.append(0)
    return


for i in arr_m:
    binary(arr_n,i)

print(*rlt)