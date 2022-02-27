import sys

sys.stdin = open('input.txt')

T = int(input())

def sol(arr):
    max_kill = 0
    for r in range(len(arr)-M+1):
        for c in range(len(arr)-M+1):
            sum_kill = 0
            for i in range(M):
                for j in range(M):
                    sum_kill += arr[i+r][j+c]
            if sum_kill > max_kill:
                max_kill = sum_kill
    return max_kill

for tc in range(1, T + 1):
    N,M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N)]
    ans = sol(matrix)
    print(f'#{tc} {ans}')

