# 첫번째 수 :양의 정수 한개 지정
N = int(input())

# 최대 개수 리스트 선언
max_lst = []
for i in range(N//2,N+1):
    num1 = N
    lst = [N]
    # 두번째 수 : 양의 정수 중 하나 선택
    num2 = i
    lst.append(num2)
    while True:
        # 세번쨰 수 : 첫번째 수 - 두번째 수
        num3 = num1 - num2
        if num3 < 0:
            if len(lst) > len(max_lst):
                max_lst = lst
            else:
                break
        else:
            lst.append(num3)
            num1 , num2 = num2, num3

print(len(max_lst))
for num in max_lst:
    print(num,end=' ')