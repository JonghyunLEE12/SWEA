import sys

sys.stdin = open('input.txt')

T = 2
def sol(string):
    stack=[]
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False

    return True

for tc in range(1, T + 1):
    problem = input()
    sol(problem)
    print(f'#{tc} {sol(problem)}')

