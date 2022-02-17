import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    rlt_list=[]
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        rlt_list.append(cnt)

    max_cnt = rlt_list[0]
    for k in rlt_list:
        if k > max_cnt:
            max_cnt = k
    print(f'#{tc} {max_cnt}')

