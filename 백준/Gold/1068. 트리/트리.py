n = int(input())
arr = list(map(int,input().split(' ')))
rm = int(input())


count = 0

def dfs(num,arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i,arr)

dfs(rm,arr)
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)