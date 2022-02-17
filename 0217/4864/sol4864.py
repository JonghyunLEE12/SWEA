import sys

sys.stdin = open('input.txt')

T = int(input())

def check(str1,str2):
    if str1 in str2:
        return 1
    return 0


for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    print(f'#{tc} {check(str1,str2)}')

