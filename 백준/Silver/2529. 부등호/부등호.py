'''
9
> < < < > > > < <
'''

k = int(input())
op = list(input().split())

numbers = [ _ for _ in range(10)]
visited = [0]* 10

max_num , min_num = "", ""


def check(x,y,op):
    if op == '<':
        if x > y :
            return False
    elif op == '>':
        if x < y :
            return False 

    return True

def dfs(depth,s):
    
    global max_num, min_num

    if depth == k+1:
        if not len(min_num):
            min_num = s
        else:
            max_num = s
        return 


    for i in range(10):
        if visited[i] == 1:
            continue


        if depth == 0 or check(s[-1],str(i),op[depth -1]):
            visited[i] = 1
            dfs(depth + 1 , s + str(i))
            visited[i] = 0


dfs(0,"")


print(max_num)
print(min_num)
