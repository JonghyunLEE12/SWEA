import sys

sys.stdin = open('input.txt')

'''
matrix의 중앙값을 구해 준 뒤,
sol1 에서는
왼쪽 + 중앙 , 오른쪽 + 중앙 을 해줬습니다.
두개의 합의 차를 구해주고
두개의 합의 차와 중앙값 인덱스의 합이 같으면 True 아니면 False 를 return  했습니다.

sol2 에서는
matrix 를 상 , 하 부분을 나눴고 sol1 과 같이 진행 하였습니다.

sol1 과 sol2 가 둘다 True 일때 1 출력 
'''

T = int(input())

def sol1(arr):
    L = len(arr)//2
    sum_1 = 0
    for i in range(len(arr)):
        for j in range(L+1):
            sum_1 += arr[i][j]
    sum_2 = 0
    for a in range(len(arr)):
        for b in range(L,len(arr)):
            sum_2 += arr[a][b]

    if sum_1 > sum_2:
        rlt = sum_1 - sum_2
    else:
        rlt = sum_2 - sum_1

    middle = 0
    for r in range(len(arr)):
        for c in range(L,L+1):
            middle += arr[r][c]

    if rlt == middle:
        return True
    else:
        return False

def sol2(arr):
    L = len(arr)//2
    sum_1 = 0
    for i in range(L+1):
        for j in range(len(arr)):
            sum_1 += arr[i][j]
    sum_2 = 0
    for a in range(L,len(arr)):
        for b in range(len(arr)):
            sum_2 += arr[a][b]
    if sum_1 > sum_2:
        rlt = sum_1 - sum_2
    else:
        rlt = sum_2 - sum_1
    middle = 0
    for r in range(L,L+1):
        for c in range(len(arr)):
            middle += arr[r][c]

    if rlt == middle:
        return True
    else:
        return False


for tc in range(1, T + 1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N)]
    if sol1(matrix) and sol2(matrix) :
        ans = 1
    else :
        ans = 0
    print(f'#{tc} {ans}')

