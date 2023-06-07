n,m = map(int,input().split(' '))

arr1 = [ list(map(int,input().split(' '))) for _ in range(n)]
arr2 = [ list(map(int,input().split(' '))) for _ in range(n)]

new_arr = []

def plus(arr1,arr2):
    plus_arr = []
    for i in range(m):
        plus_arr.append(arr1[i] + arr2[i])
    return plus_arr


for i in range(n):
    new_arr.append(plus(arr1[i],arr2[i]))

for arr in new_arr:
    print(*arr)