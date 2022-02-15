import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    page, page_a, page_b = map(int, input().split())
    page_list = [0]*(page+2)
    for i in range(1, page + 1):
        page_list[i] = i
    left_a = page_list[0]
    right_a = page_list[page - 1]
    left_b = page_list[0]
    right_b = page_list[page - 1]
    rlt_a = 0
    rlt_b = 0

    while left_a <= right_a :
        mid_a = int((left_a + right_a) // 2)
        mid_b = int((left_b + right_b) // 2)
        if page_list[mid_a] == page_a:
            rlt = 'A'
            break
        elif page_list[mid_a] > page_a:
            right_a = mid_a - 1
        else:
            left_a = mid_a + 1
        if page_list[mid_b] == page_b:
            if rlt == 'A':
                rlt = 0
                break
            rlt = 'B'
            break
        elif page_list[mid_b] > page_b:
            right_b = mid_b - 1
        else:
            left_b = mid_b + 1

    print(f'#{tc} {rlt}')