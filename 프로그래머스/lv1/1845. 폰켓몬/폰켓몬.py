def solution(nums):
    choose = int(len(nums) / 2) 
    nums = set(nums) 
    
    answer = min(len(nums), choose)
    
    return answer