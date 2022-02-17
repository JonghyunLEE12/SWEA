import sys

sys.stdin = open('input.txt')

T = 10


def pali(arr):
    for l in range(100,-1,-1):              # l은 100에서 하나씩 감소 범위를 점점 줄여가며 회문을 찾음
        for i in range(100):                # i는 0에서 부터 증가
            for j in range(100-l + 1):      # j는 100 - l
                pal = arr[i][j:j+l]
                if pal == pal[::-1]:
                    return l

def sero(arr):
    col_list=[]
    for col in range(len(arr[0])):
        lst = []
        for row in range(len(arr)):
            lst.append(arr[row][col])
        col_list.append(lst)

    return col_list

for tc in range(1, T + 1):
    N = int(input())
    words = [list(input()) for _ in range(100)]
    words_sero = sero(words)

    rlt_words=pali(words)
    rlt_sero=pali(words_sero)
    if rlt_words > rlt_sero:
        rlt = rlt_words
    else:
        rlt = rlt_sero

    print(f'#{tc} {rlt}')

