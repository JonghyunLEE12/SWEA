import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    sum_num = 0
    for i in range(1,N+1):
        if i % 2:
            sum_num += i
        else :
            sum_num -= i
    print(f'#{tc} {sum_num}')

