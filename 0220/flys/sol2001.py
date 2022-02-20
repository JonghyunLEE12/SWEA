import sys

sys.stdin = open('input.txt')

T = int(input())

def flys(arr):
    max_kill = 0
    L = len(arr)
    for i in range(L-M+1):
        for j in range(L-M+1):
            sum_kill = 0
            for a in range(M):
                for b in range(M):
                    sum_kill += arr[i+a][j+b]
            if sum_kill > max_kill:
                max_kill = sum_kill
    return max_kill

for tc in range(1, T + 1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc} {flys(matrix)}')

