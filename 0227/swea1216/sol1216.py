import sys

sys.stdin = open('input.txt')

T = 10
def pali(arr):
    for n in range(len(arr),-1,-1):
        for r in range(len(arr)):
            for c in range(len(arr)-n+1):
                pal = arr[r][c:c+n]
                if pal == pal[::-1]:
                    return n

for tc in range(1, T + 1):
    N = int(input())
    matrix = [input() for _ in range(100)]
    matrix_trans = list(map(list,zip(*matrix)))
    ans1 = pali(matrix)
    ans2 = pali(matrix_trans)
    if ans1 > ans2:
        rlt = ans1
    else:
        rlt = ans2
    print(f'#{tc} {rlt}')

