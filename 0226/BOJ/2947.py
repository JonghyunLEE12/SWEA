

lst = list(map(int,input().split()))
cnt = 0
for i in range(len(lst) - 1):
    for j in range(i, len(lst)):
        if lst[i] > lst[j]:
            print(*lst)
            lst[i], lst[j] = lst[j], lst[i]
            cnt += 1

        if lst  == [1,2,3,4,5]:
            break