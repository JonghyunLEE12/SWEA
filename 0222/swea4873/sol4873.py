import sys

sys.stdin = open('input.txt')

T = int(input())

def check(string):
    stack = []                                  # stack 리스트 선언
    for alpha in string:                        # 문자열을 순회
        if stack and alpha == stack[-1]:        # stack 이 true 이면서, 현재 alpha 가 stack 의 마지막 값 과 같으면,
            stack.pop()                         # pop
        else:
            stack.append(alpha)                 # if를 만족하지 못했을때, push
    return stack


for tc in range(1, T + 1):
    string = input()
    check(string)
    print(f'#{tc} {len(check(string))}')

