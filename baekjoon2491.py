N = int(input())
numbers = list(map(int,input().split()))

cnt = 1
##커질때
for i in range(2,len(numbers)):
    if numbers[i-1] >= numbers[i-2]:
        if numbers[i] >= numbers[i-1]:
            cnt+=1

print(cnt)




