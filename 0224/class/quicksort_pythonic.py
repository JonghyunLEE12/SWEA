def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    other = arr[1:]

    # 피봇보다 작은애들 다 두기
    left = [ x for x in other if x <= pivot]
    right = [ x for x in other if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

lst = [69,100,30,2,16,8,31,22]
print(lst)
print(quicksort(arr=lst))
