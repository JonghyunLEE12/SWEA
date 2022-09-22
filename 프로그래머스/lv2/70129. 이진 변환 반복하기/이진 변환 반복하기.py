def solution(s):
    answer = []
    count , count_0 = 0,0
    while True:
        new_s = ''
        
        for i in s:
            if i == '0':
                count_0 += 1
                continue
            elif i == '1':
                new_s += i
        
        new = ''
        num = len(new_s)
        while True:
            if num == 1:
                new += str(num)
                break
            new += str(num%2)
            num = num // 2
        
        new = new[::-1]
        
        s = new
        count += 1
        if new == '1':
            break
                
            
    answer = [count , count_0]
    return answer