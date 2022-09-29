def check(arr,i):
    stack = []
    for j in range(len(arr)):
        if arr[0] in [']','}',')']:
            return False
        else:
            if j == 0 or arr[j] in ['{','(','[']:
                stack.append(arr[j])
                continue
            if arr[j] == ')':
                if '(' in stack:
                    stack.pop()
            if arr[j] == '}':
                if '{' in stack:
                    stack.pop()
            if arr[j] == ']':
                if '[' in stack:
                    stack.pop()
    if len(stack) != 0:
        return False
    return True

def solution(s):
    answer = -1
    answer_s = s
    count = 0
    i = 0
    while True:
        if check(s,i) == True:
            count += 1
        next_s = s[1:] + s[0]
        s = next_s
        if next_s == answer_s:
            break
        i += 1
    return count