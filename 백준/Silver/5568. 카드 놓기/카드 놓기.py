n = int(input())
k = int(input())

numbers = [ str(input()) for x in range(n)]
visited = [0]*len(numbers)

rlt = set()


def dfs(start,arr):
    if len(arr) == k:
        rlt.add("".join(arr))
        return

    for i in range(len(numbers)):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(numbers[i])
            dfs(i,arr)
            arr.pop()
            visited[i] = 0

for i in range(len(numbers)):
    if visited[i] == 0:
        visited[i] = 1
        arr = [numbers[i]]
        dfs(i,arr)
        arr.pop()
        visited[i] = 0





print(len(rlt))