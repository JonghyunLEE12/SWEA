
n,m = map(int,input().split(' '))
items = []


for _ in range(n):
    v,c,k = map(int,input().split(' '))
    count = 1
    while k > 0:
        take = min(count,k)
        items.append((v * take, c * take))
        k -= take
        count *= 2


dp = [0] * (m+1)

for w,s in items:
    for j in range(m, w -1, -1):
        dp[j] = max(dp[j], dp[j - w] + s)
        
print(dp[m])
