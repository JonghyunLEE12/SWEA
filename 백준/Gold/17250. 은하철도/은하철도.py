def Find(x):

    if x!=disjoint[x]:
        disjoint[x]=Find(disjoint[x])

    return disjoint[x]

def Union(a,b):

    a=Find(a)
    b=Find(b)

    if a>b:
        disjoint[a]=b
        dp[b]+=dp[a]
    elif a<b: #똑같은 경로는 더하면 안됨.
        disjoint[b]=a
        dp[a]+=dp[b]

N,M=map(int,input().split())

disjoint=[0]*(N+1)

for i in range(1,N+1):
    disjoint[i]=i

dp=[0]*(N+1)

for i in range(N):
    dp[i+1]=int(input())


for i in range(M):

    a,b=map(int,input().split())
    Union(a,b)
    print(dp[min(Find(a),Find(b))])