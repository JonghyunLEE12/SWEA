import sys

sys.stdin = open('input.txt')

T = int(input())

def sol(arr):
    stack = []                      # stack 생성
    op = ['+','/','*','-']          # 연산자 리스트
    for i in arr:                   # arr를 순회하며
        if i in op:                 # i 가 연산자 리스트 안에 있는 경우
            stack.append(i)         # stack에 추가
            arr.remove(i)           # 기존 arr 에서 제거
    for j in range(len(stack)):     # 위의 for 문 종료 후, stack을 순회하며
        arr.append(stack.pop())     # pop을 사용하여 뒤에 부터 arr 에 저장
    return arr

for tc in range(1, T + 1):
    arr = list(input())
    rlt = sol(arr)
    print(f'#{tc}',end=' ')
    for i in rlt:
        print(i,end='')
    print()

