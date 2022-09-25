def change_2(num):
    n_copy = num
    n_2 = ''
    while True:
        if n_copy == 1:
            n_2 += str(n_copy)
            n_2 = n_2[::-1]
            break
        n_2 += str(n_copy%2)
        n_copy = n_copy // 2
    return n_2

def solution(n):
    
    answer = 0
    # 1 answser > n
    # 2 n의 2진수와 answer의 2진수의 1의 개수가 같음
    # 3 n의 다음 큰 숫자는 1,2 를 만족하는 가장 작은 수
    
    n_2 = change_2(n)
    # print(n_2.count('1'))
    
    while True:
        if answer != 0:
            break
        
        n += 1
        
        next_n_2 = change_2(n)
        if n_2.count('1') == next_n_2.count('1'):
            answer += n
    
        
        
    
    
    
        
    return answer