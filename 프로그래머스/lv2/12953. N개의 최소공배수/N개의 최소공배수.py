# def solution(arr):
#     answer = 0
#     arr.sort()
#     m = arr[-1]
#     answer = m 
#     while True:
#         for i in range(len(arr)-1):
#             if answer % arr[i] != 0:
#                 break
#             else:
#                 return answer
#             answer += m
#     return answer

def solution(arr):
    arr.sort()
    m = arr[-1]
    answer = m
    while True:
        for i in range(len(arr)-1):
            if answer % arr[i] != 0:
                break
        else:
            return answer
        answer += m