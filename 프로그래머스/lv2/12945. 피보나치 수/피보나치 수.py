# def fibo(n):
#     global sum
    
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     sum = fibo(n-1) + fibo(n-2) 
    
#     return sum

# def solution(n):
#     answer = 0
#     sum = 0
    
#     answer = fibo(n) % 1234567
    
    
#     return answer


def solution(n):
    answer = 0
    
    a = [0] * (n+1)
    a[1] = 1
    for i in range(2,n+1):
        a[i] = ( a[i-1] + a[i-2] ) % 1234567
    
    return a[n]
    
    return answer 