n,m = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()

stack = []

def dfs():
    global stack

    if len(stack) == m:
        print(*stack)
        return
    for i in range(n):
        stack.append(numbers[i])
        dfs()
        stack.pop()


dfs()