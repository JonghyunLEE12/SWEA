import sys

sys.stdin = open('input.txt')

T = int(input())

def change(money):
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_num = [0]*8
    for i in range(8):
        if money // money_list[i]:
            money_num[i] += money // money_list[i]
            money = money % money_list[i]
    return money_num

for tc in range(1, T + 1):
    N = int(input())
    rlt = change(N)
    print(f'#{tc}')
    print(*rlt)

