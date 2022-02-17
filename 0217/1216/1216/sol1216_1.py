import sys

sys.stdin = open('input.txt')

T = 10


def pali(arr):
    for num in range(len(arr),-1,-1):               # 큰수부터 줄여가며 회문인지를 판별,
        for i in range(len(arr)):
            for j in range(len(arr)-num+1):         # j 부터 j+num까지 판단해야 하기 때문
                pal = arr[i][j:j+num]               # j 부터 j+num 의 문자열이 회문인지를 판단
                if pal == pal[::-1]:                # 회문 인 경우, 해당 num 값을 출력
                    return num



def transpose(arr):                                 # 세로 방향으로 돌려주는 함수
    col_list = []
    for i in range(len(arr[0])):
        lst = []
        for j in range(len(arr)):
            lst.append(arr[j][i])
        col_list.append(lst)
    return col_list


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(100)]
    trans_matrix = transpose(matrix)

    rlt_a = pali(matrix)                            # 가로 방향 회문 최대값
    rlt_b = pali(trans_matrix)                      # 세로 방향 회문 최대 값
    if rlt_a > rlt_b:                               # 두개의 크기 비교 후 출력
        rlt = rlt_a
    else :
        rlt = rlt_b
    print(f'#{tc} {rlt}')

