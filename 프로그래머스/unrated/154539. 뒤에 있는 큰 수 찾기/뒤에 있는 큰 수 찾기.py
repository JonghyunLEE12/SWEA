# def solution(numbers):
#     answer = []

#     def checking(arr,target):
#         for i in arr:
#             if i > target:
#                 return i
#         return -1
        
#     for i in range(len(numbers)):
#         add_num = checking(numbers[i:],numbers[i])
#         answer.append(add_num)
#     return answer


def solution(numbers):
    stack = []
    answer = [0] * len(numbers)        

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    while stack:
            answer[stack.pop()] = -1
    
    return answer