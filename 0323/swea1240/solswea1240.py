import sys
import pprint
sys.stdin = open('input.txt')
# 0 ~ 9까지의 수와 대응하는 이진 코드
P = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
T = int(input())


'''
 - 검증코드는 아래와 같은 방법으로 계산한다.

    “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.
'''

def find_row():
    global target
    flag = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == '1':
                target = matrix[i]
                flag = 1
                break
        if flag == 1:
            break
    return

for tc in range(1, T + 1):
    n,m = map(int,input().split())
    matrix = [list(map(str,input())) for _ in range(n)]
    target = []

    find_row()
    # target 에 2진수 열 저장
    # 마지막 1을 찾기위해 역순으로 저장
    p = m-target[::-1].index('1')
    target = target[p-56:p]
    # 0부터
    rlt = []
    for i in range(0,len(target),7):
        code = target[i:i+7]
        rlt.append("".join(code))

    num_list = []
    for i in rlt:
        number = P.get(i)
        num_list.append(number)

    ans = 0
    odd = 0
    even = 0

    for i in range(len(num_list)-1):
        # 홀수 이면
        if i%2:
            odd += num_list[i]
        # 짝수이면
        else:
            even += num_list[i]
    ans = odd + even*3 + num_list[-1]
    if ans % 10 == 0:
        ans = odd+even+num_list[-1]
    else:
        ans = 0


    print(f'#{tc} {ans}')

