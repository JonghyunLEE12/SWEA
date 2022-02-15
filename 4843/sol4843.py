import sys

sys.stdin = open('input.txt')

T = int(input())
# N개의 정수가 주어지면, 가장 큰 수, 가장 작은 수 2번째 큰 수, 두번째 작은수를 번갈아 가면서 정렬
def bubble_sort(arr):                           # 버블 소트 함수 선언
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr                                  # 내림차순으로 정렬 된다.

def special_sort(arr):                          # special sort 함수 선언
    sorted_arr = []                             # 정렬된 리스트를 담을 비어있는 리스트 선언
    while True:
        if len(arr) == 0:                       # 기존 배열의 크기가 0이 되면, break
            break
        sorted_arr.append(bubble_sort(arr)[0])  # 내림차순 정렬된 값 중 가장 큰 값 append
        sorted_arr.append(bubble_sort(arr)[-1]) # 내림차순 정렬된 값 중 가장 작은 값 apend
        arr = arr[1:len(arr)-1]                 # append 된 값들 제거

    return sorted_arr                           # 정렬이 완료된 값



for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int,input().split()))
    rlt = special_sort(numbers)
    print(f'#{tc}',end=' ')
    print(*rlt[:10])                            # 10개만 출력
