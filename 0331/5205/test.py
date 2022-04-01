import sys

sys.stdin = open('input.txt')

T = int(input())


def quick_sort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quick_sort(a, l, s - 1)  # 피봇 기준 왼쪽 정렬
        quick_sort(a, s + 1, r)  # 피봇 기준 오른쪽 정렬

def partition(a, l, r):
    p = a[l]  # p: 피봇 값
    i = l + 1  # 첫 번째 값은 피봇으로 사용함
    j = r

    while i <= j:
        while i <= j and a[i] <= p:  # i는 피봇보다 큰 값을 가리킴
            i += 1
        while i <= j and a[j] >= p:  # j는 피봇보다 작은 값을 가리킴
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]  # 작은값은 왼쪽, 큰값은 오른쪽

    a[l], a[j] = a[j], a[l]  # 피봇을 작은값과 큰값의 센터에 둠

    return j


for tc in range(1, T + 1):
    n = int(input())
    array = list(map(int, input().split()))

    quick_sort(array, 0, len(array) - 1)
    print(f'#{tc} {array[n//2]}')