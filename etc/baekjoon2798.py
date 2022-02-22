#블랙잭

#N 과 M 을 입력 받아.
N , M = map(int,input().split())

#카드의 리스트가 나옴
card_list= list(map(int,input().split()))

def black_jack(card_list):
    result_total=[]
    for number1 in range(N):
        for number2 in range(number1 , N):
            for number3 in range(number2,N):
                total = card_list[number1] + card_list[number2] + card_list[number3] 
                if total > M:
                    continue
                else :
                    result_total.append(total)
                    result = max(result_total)
    return result

print(black_jack(card_list))


