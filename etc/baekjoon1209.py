testcase = 10
for tc in range(1,testcase+1):
    lst = []
    for i in range(100):
        sub = list(map(int,input().split()))
        lst.append(sub)

    rlt_lst = []

    # 각 행의 합
    
    for y in range(len(lst)):
        sum_row = 0
        for x in range(len(lst)):
            sum_row += lst[y][x]
        rlt_lst.append(sum_row)
    # 각 열의 합
    
    for x in range(len(lst)):
        sum_col = 0
        for y in range(len(lst)):
            sum_col += lst[y][x]
        rlt_lst.append(sum_col)
    
    # 대각선의 합
    sum_1 = 0
    for y in range(len(lst)):
        for x in range(len(lst)):
            if y == x:
                sum_1 += lst[y][x]
    rlt_lst.append(sum_1)
    
    # 역 대각선의 합
    sum_2 = 0
    for y in range(len(lst)):
        for x in range(len(lst)):
            if y == len(lst)-x:
                sum_2 += lst[y][x]
    rlt_lst.append(sum_2)
    
    result = max(rlt_lst)

    print(f'#{tc} {result}')



