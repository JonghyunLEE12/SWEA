def powerset(idx,sum_num):
    if sum_num > 10:
        return
    if idx == N:
        if sum_num == 10:
            for i in range(N):
                if bit[i]:
                    print(arr[i],end=' ')
            print()
        return

    else:
        bit[idx] = 0
        powerset(idx+1,sum_num)

        bit[idx] = 1
        powerset(idx+1,sum_num+arr[idx])
        
arr = [x for x in range(1,11)]
N = len(arr)
bit = [0] * N
powerset(0,0)