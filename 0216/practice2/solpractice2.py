import sys

sys.stdin = open('input.txt')

T = int(input())
def itoa(number):
    ord_list =[]                        # ord 를 이용해 변경한 값을 담을 리스트 선언
    for i in number:
        ord_list.append(ord(i))
    chr_list=[]                         # chr 를 이용해 변경한 값을 담을 리스트 선언
    for j in ord_list:
        chr_list.append(chr(j))
    return chr_list


for tc in range(1, T + 1):
    number = input()
    rlt = itoa(number)
    print(f'#{tc} {"".join(rlt)} {type("".join(rlt))}')

