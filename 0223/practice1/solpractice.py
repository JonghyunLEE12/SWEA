import sys

sys.stdin = open('input.txt')

T = int(input())

def sol(arr):
    stack = []
    res = ''
    for x in arr:
        if x.isdecimal():
            res += x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()
    return res
for tc in range(1, T + 1):
    arr = list(input())
    rlt = sol(arr)
    print(f'#{tc} {rlt}')

