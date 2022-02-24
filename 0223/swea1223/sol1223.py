import sys

sys.stdin = open('input.txt')

T = 10
def pre(string):
    stack = []                                      # stack 생성
    rlt = ''                                        # pre로 치환 될 문자열을 담을 rlt 선언
    for i in string:
        if i.isdecimal():                           # isdecimal => i 가 숫자로 된 문자열인가??
            rlt += i                                # rlt 에 담아둬
        else :
            if i == '+':                            # i 가 + 일때,
                while stack:                        # stack 이 비었을때, 종료
                    rlt += stack.pop()
                stack.append(i)
            elif i == '*':                          # i 가 * 일때,
                while stack and stack[-1] == '*':   # stack이 False 이거나 stack의 top 이 * 이 아니게 되면 종료
                    rlt += stack.pop()
                stack.append(i)
    for i in stack:                                 # stack에 남아 있는 연산자들 문자열에 저장
        rlt += i
    return rlt

def sol(string):
    stack = []                                      # stack 생성
    for i in string:
        if i.isdecimal():                           # i 가 숫자로 이루어진 문자열 일 때,
            stack.append(int(i))                    # int형으로 변경하여 stack에 저장
        else:
            num1= stack.pop()                       # i 가 연산자일때, stack에 저장된 값들을 num1, num2 에 저장
            num2= stack.pop()
            if i =='+':                             # i 가 + 일때,
                stack.append(num1+num2)             # +값 stack 에 저장
            elif i == '*':                          # i 가 * 일때,
                stack.append(num1*num2)             # *값 stack 에 저장
    return stack.pop()

for tc in range(1, T + 1):
    # isdecimal() 주어진 문자열이 숫자로 되어 있는지 판단하는 함수
    N = int(input())
    string = input()
    rlt = pre(string)
    ans = sol(rlt)
    print(f'#{tc} {ans}')

