import sys

sys.stdin = open('input.txt')

T = int(input())

def binary(p,target):                   # binary 함수 선언
    start = 1                           # start = 1
    end = p                             # end = page 숫자
    cnt = 0                             # cnt 0 으로 초기화
    while True:
        middle = (start+end)//2         # 중간값을 찾은후
        if middle > target:             # 중간값이 target 보다 클 경우
            end = middle                # end 값 변경
            cnt += 1                    # cnt 증가
        elif middle < target:           # 중간값이 target 보다 작을 경우
            start = middle              # start 값 변경
            cnt += 1                    # cnt 증가
        if middle == target:            # middle 이 target 과 같을 때 break
            break
        if start >= end:                # start 가 end 와 같거나 넘었을 때  break
            break
    return cnt


for tc in range(1, T + 1):
    p,a,b = map(int,input().split())
    rlt_a = binary(p,a)
    rlt_b = binary(p,b)
    if rlt_a < rlt_b:
        winner = 'A'
    elif rlt_a > rlt_b:
        winner = 'B'
    else :
        winner = 0

    print(f'#{tc} {winner} ')

