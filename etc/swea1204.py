#최빈수 구하기
T=int(input())
for tc in (1,T+1):
    numbers=list(map(int,input('').split()))
    _max = 0

    for value in range(101):
        if numbers.count(value)==0:
            continue
        elif numbers.count(value) >= array.count(_max):
            _max=value
    
    print(f'#{tc} {_max}')


            
