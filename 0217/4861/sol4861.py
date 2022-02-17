import sys


sys.stdin = open('input.txt')

T = int(input())

def pali(arr):
    # 가로 줄 탐색
    # 가로 회문 찾기
    for i in range(len(arr)):
        for j in range(len(arr[i]) - (M-1)):
            pal = arr[i][j:j+M]
        if pal == pal[::-1]:
            return pal

    # 세로 줄 탐색
    col_list = []
    for col in range(len(arr[0])):
        lst = []
        for row in range(len(arr)):
            lst.append(arr[row][col])
        col_list.append(lst)

    for i in range(len(col_list)):
        for j in range(len(col_list) - (M-1)):
            pal = col_list[i][j:j+M]
        if pal == pal[::-1]:
            return pal

for tc in range(1, T + 1):
    N , M = map(int,input().split())
    matrix = [list(input()) for _ in range(N)]
    print(f'#{tc}',end=' ')
    print("".join(pali(matrix)))

