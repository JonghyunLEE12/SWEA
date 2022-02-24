def partition(arr, start, end):
    pivot = arr[(start + end) // 2]
    while start <= end:
        # start
        while arr[start] < pivot:
            start += 1
        # end
        while arr[end] > pivot:
            end -= 1
        if start <= end:  # 엇갈리지 않았다면
            arr[start], arr[end] = arr[end], arr[start]  # swap
            start += 1
            end -= 1
    return start


def quicksort(arr, start, end):
    part2_idx = partition(arr, start, end)
    if start < end:
        quicksort(arr, start, part2_idx - 1)
        quicksort(arr, part2_idx, end)


lst = [69, 10, 30, 2, 16, 2, 2, 2, 8, 31, 22]
print(lst)

quicksort(arr=lst, start=0, end=len(lst) - 1)
print(lst)