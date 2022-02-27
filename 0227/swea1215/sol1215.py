import sys

sys.stdin = open('input.txt')

T = 10

def pali(arr):
    count = 0
    for r in range(len(arr)):
        for c in range(len(arr)-N+1):
            pal = arr[r][c:c+N]
            if pal == pal[::-1]:
                count += 1
    return count

for tc in range(1, T + 1):
    N = int(input())
    matrix = [ input() for _ in range(8)]
    matrix_transpose = list(map(list,zip(*matrix)))
    ans = pali(matrix) + pali(matrix_transpose)
    print(f'#{tc} {ans}')

