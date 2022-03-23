# A의 부분집합 중 합이 K인 부분집합의 개수 구하기


def f (i,N,S,K): # s i-1 원소가지 고려된 부분집합의 합
    global cnt
    if i == N:
        if S == K:
            cnt += 1
    else:
        f(i+1,N,S+A[i],K) # A[i]포함
        f(i+1,N,S,K) # 포함 되지 않음



A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
# 0 번부터 가고  길이는 N 이고 합은 0 이야
cnt = 0
K = 55
f(0,N,0,K)
print(cnt)