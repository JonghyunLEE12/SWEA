n=int(input())
def fibo (n):
    if n<2:
        return n
    return n + fibo(n-2)
print(fibo(n)) 