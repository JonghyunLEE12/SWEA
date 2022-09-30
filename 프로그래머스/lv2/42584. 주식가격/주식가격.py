from collections import deque

def check(arr):
    stack = [-1]*len(arr)
    
    for i in range(len(arr)):
        for j in range(i,len(stack)):
            if arr[i] <= arr[j]:
                stack[i] += 1
            else:
                stack[i] += 1
                break
    return stack

def solution(prices):
    answer = check(prices)
    return answer