import sys

sys.stdin = open('input.txt')

T = 10

def pre(op):
    stack = []
    rlt = []
    for token in op:
        if token.isdigit():
            rlt.append(token)
        else:
            if token == '(':
                stack.append(token)
            elif token == ')':
                temp = stack.pop()
                while temp != '(':
                    rlt.append(temp)
                    temp = stack.pop()
            elif token == '*' :
                while stack and stack[-1] == '*':
                    rlt.append(stack.pop())
                stack.append(token)
            elif token == '+' :
                while stack and stack[-1] != '(':
                    rlt.append(stack.pop())
                stack.append(token)
    for _ in range(len(stack)):
        rlt.append(stack.pop())
    return rlt

def sol(rlt):
    stack = []
    for i in rlt:
        if i.isdigit():
            stack.append(int(i))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':
                stack.append(num1+num2)
            elif i == '*':
                stack.append(num1*num2)
    ans = stack.pop()
    return ans

for tc in range(1, T + 1):
    N = int(input())
    op = list(input())
    rlt = pre(op)
    ans = sol(rlt)
    print(f'#{tc} {ans}')

