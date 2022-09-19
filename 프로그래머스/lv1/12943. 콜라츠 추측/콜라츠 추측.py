def solution(num):
    answer = 0
    
    cnt = 0
    
    while True:
        cnt += 1
        if cnt == 500 or num == 1:
            break
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
    if cnt == 500:
        cnt = -1
    else:
        cnt -= 1
    return cnt