import sys

sys.stdin = open('input.txt')

T = int(input())

def flys(arr):
    max_sum=0
    for a in range(len(arr)-M+1):
        for b in range(len(arr)-M+1):
            sum_num = 0
            for i in range(M):
                for j in range(M):
                    sum_num += arr[a+i][b+j]
            if sum_num > max_sum:
                max_sum = sum_num
    return  max_sum

for tc in range(1, T + 1):
    N , M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc} {flys(matrix)}')

