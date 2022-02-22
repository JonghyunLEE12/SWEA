import sys

sys.stdin = open('input.txt')

T = int(input())

def check(string):
    stack = []
    for word in string:
        if word == '{':                         # stack 에 저장
            stack.append(word)
        if word == '(':                         # stack 에 저장
            stack.append(word)
        if word == ')':                         # ) 가 나왔을 때,
            if stack and stack[-1] == '(':      # stack이 False 가 아니고, stack에 저장된 값중 마지막이 '(' 라면
                stack.pop()                     # pop
            else:
                return 0                        # 조건 만족을 안했을 경우 0 출력
        if word == '}':                         # } 가 나왔을 때,
            if stack and stack[-1] == '{':      # stack 이 False 가 아니고, stack에 저장된 값중 마지막이 '{' 라면
                stack.pop()                     # pop
            else:
                return 0                        # 조검 만족 안했을 경우 0 출력
    if len(stack) == 0:                         # 만약 stack에 값이 없다면
        return 1                                # 1 출력
    else:
        return 0                                # stack에 값이 남아 있을 경우 0 출력
for tc in range(1, T + 1):
    string = input()
    print(f'#{tc} {check(string)}')

