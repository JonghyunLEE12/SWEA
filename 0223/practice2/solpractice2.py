def powerset(idx,sum_num):
    if sum_num > 10:                            # sum_num 의 값이 10을 넘었을때,
        return                                  # 종료
    if idx == N:                                # 현재 idx 가 10 일때,
        if sum_num == 10:                       # sum_num 이 10 이면
            for i in range(N):
                if bit[i]:                      # 더해서 합이 10이 된 부분집합의 인덱스만 출력
                    print(arr[i],end=' ')
            print()
        return
    else:
        bit[idx] = 0
        powerset(idx+1,sum_num)

        bit[idx] = 1                            # bit 배열의 해당 idx 가 1 일 때,
        powerset(idx+1,sum_num + arr[idx])      # sum_num 에 해당 부분집합의 수를 더해 준다.
arr = [1,2,3,4,5,6,7,8,9,10]
N = len(arr)
bit = [0] * N
powerset(0,0)

