import sys

sys.stdin = open('input.txt')

T = int(input())


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    rest = arr[1:] # 피봇 데이터를 제외한 리스트
    left = [x for x in rest if x <= pivot] # pivot 보다 작거나 같은 값 저장
    right = [x for x in rest if x > pivot] # pivot 보다 큰 값 저장

    return quick_sort(left) + [pivot] + quick_sort(right)


for tc in range(1,T+1):
    numbers = list(map(int, input().split()))
    ans = quick_sort(numbers)
    print(f'#{tc}',end=' ')
    print(*ans)