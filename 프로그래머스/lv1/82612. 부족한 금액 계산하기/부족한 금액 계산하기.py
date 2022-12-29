def solution(price, money, count):
    answer = -1
    
    # 이용금액 , 가지고 있는돈, 놀이공원 탄 횟수
    # n 배 씩 증가
    
    total = 0
    for i in range(1,count+1):
        total += price * i
    
    answer = total - money
    
    if answer < 0:
        answer = 0
    return answer