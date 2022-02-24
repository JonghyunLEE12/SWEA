import sys

sys.stdin = open('input.txt')

T = int(input())

def sol(arr):
    stack = []
    try:
        for i in arr:
            if i == '.':
                if len(stack) > 1:
                    ans = 'error'
                    return ans
                else :
                    ans = stack.pop()
                    return ans
            elif i.isdecimal():
                stack.append(int(i))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == '*':
                    stack.append(num1*num2)
                elif i == '/':
                    stack.append(num1//num2)
                elif i == '+':
                    stack.append(num1+num2)
                elif i =='-':
                    stack.append(num1-num2)
    except:
        ans = 'error'
        return ans


for tc in range(1, T + 1):
    operation = list(input().split())
    ans = sol(operation)
    print(f'#{tc} {ans}')