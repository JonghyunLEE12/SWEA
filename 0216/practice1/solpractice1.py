import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    string = input()                # 문자열 입력 받음
    str_lst = list(string)          # 받은 문자열을 리스트 형태로 바꿔주고
    str_lst.reverse()               # reverse() 메소드 사용
    print(f'#{tc} {"".join(str_lst)}') # join을 이용하여 출력

