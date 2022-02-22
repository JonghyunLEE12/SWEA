def sol(arr):
    stack = []
    for i in arr:
        if i =='(':
            stack.append(i)
        elif i == ')':
            if len(stack):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return  True
    else:
        return False
