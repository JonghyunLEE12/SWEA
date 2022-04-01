import sys

sys.stdin = open('input.txt')

T = int(input())



def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0] # 피봇
    rest = arr[1:] # 피봇제외 나머지
    left = []
    for x in rest:
        if x <= pivot:
            left.append(x)
    right = []
    for y in rest:
        if y > pivot:
            right.append(y)
    return quick_sort(left) + [pivot] + quick_sort(right)


for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int,input().split()))
    rlt = quick_sort(numbers)
    print(f'#{tc} {rlt[n//2]}')

