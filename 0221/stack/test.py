def fibo(n):
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

N = 10
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1
print(fibo(N))
print(memo)