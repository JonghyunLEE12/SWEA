T=int(input())
for i in range(1,T+1):
    chrs=list(map(int,input().split()))
    sum=0
    for i in chrs:
        if i % 2:
            sum+=i
    
    print(f'#{i} {sum}')

