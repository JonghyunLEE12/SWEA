n = int(input())
matrix = sorted(map(int,input().split(' ')))

answer = 0

def twoPointer(li,target):
    global answer

    start,end = 0, len(li)-1
    while start < end:
        s = li[start] + li[end]
        if target == s:
            answer += 1
            return
        
        elif target > s:
            start += 1
        elif target < s:
            end -= 1


for i in range(n):
    twoPointer(matrix[:i] + matrix[i+1:],matrix[i])

print(answer)
