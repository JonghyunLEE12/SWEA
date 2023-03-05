T = int(input())

def binary(N,target):
    start = 0
    end = len(N)-1

    while start <= end:
        mid = (start + end) // 2
        
        if N[mid] == target:
            return 1
        elif N[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        
    return 0
    

for _ in range(T):
    n = int(input())
    arr_n = sorted(list(map(int,input().split(' '))))

    m = int(input())
    arr_m = list(map(int,input().split(' ')))

    arr_n = list(set(arr_n))

    for i in arr_m:
        print(binary(arr_n,i))
