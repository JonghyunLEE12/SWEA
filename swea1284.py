# A사 : 1리터당 P원의 돈을 내야함
# B사 : 기본 요금이 Q원 이고 R 리터 이하인 경우만 기본요금, R리터보다 초과시 1리터 당 S
# 한달 사용하는 수도의 양이 W 라고 할 때 더 저렴한 회사를 골라 그 요금을 작성

T=int(input())
for tc in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())
    a_company = W * P
    if W <= R:
        b_company = Q
    elif W > R:
        b_company = ((W-R)*S)+Q
    
    if a_company > b_company :
        result = b_company
    elif a_company < b_company:
        result = a_company
    print(f'#{tc} {result}')

    

