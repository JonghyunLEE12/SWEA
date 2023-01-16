def solution(nums):
    answer = -1

    count = 0
    def check(number):
        for x in range(2,number):
            if number % x == 0:
                return False
        return True
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                number = nums[i]+nums[j]+nums[k]
                if check(number):
                    count += 1
                
    return count