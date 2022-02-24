import sys

sys.stdin = open('input.txt')

T = 10
def pre(string):
    rlt = ''
    stack = []
    for i in string:
        if i.isdecimal():
            rlt += i
        else :
            if i == '*':
                while stack and stack[-1] == '*':
                    rlt += stack.pop()
                stack.append(i)
            elif i == '+':
                while stack:
                    rlt += stack.pop()
                stack.append(i)

    for i in stack:
        rlt += i
    return rlt

def sol(string):
    stack = []
    for i in string:
        if i.isdecimal():
            stack.append(int(i))
        else:
            num1= stack.pop()
            num2= stack.pop()
            if i =='+':
                stack.append(num1+num2)
            elif i == '*':
                stack.append(num1*num2)
    return stack.pop()

for tc in range(1, T + 1):
    # isdecimal() 주어진 문자열이 숫자로 되어 있는지 판단하는 함수
    N = int(input())
    string = input()
    rlt = pre(string)
    ans = sol(rlt)
    print(f'#{tc} {ans}')

