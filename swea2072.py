T=int(input())
for i in range(1,T+1):
    chrs=list(map(int,input().split()))
    sum=0
    for j in chrs:
        if j % 2:
            sum+=j
    
    print(f'#{i} {sum}')

