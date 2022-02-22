n=int(input())
def fibo (n):
    if n<2:
        return n
    
    result = [ 0 , 1 ]
    for i in range(2, n+1):
        result.append(result[i-1]+result[i-2])
    return result[-1]
print(fibo(n)) 


def fib_loop(n):
    if n < 2:
        return n
    
    result = [0, 1]
    for i in range(2, n+1): # list에 0의 값이 포함되어 있기 때문에 자리를 차지해서 +1만큼 계산을 더함.
        result.append(result[i-1] + result[i-2])
        # result.append(result[len(result)-1] + result[len(result)-2])
    return result[-1] # list 의 마지막 값 출력