def solution(num_list):
    answer = 0
    
    def ans(num_list):
        total = 1
        for num in num_list:
            total *= num
        return total
    
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        answer = ans(num_list)
    return answer