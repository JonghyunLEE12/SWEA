from collections import deque

n,k = map(int,input().split(' '))
cnt = 0
max_size = 100001
check = [-1] * max_size

def bfs():
    global cnt
    check[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        subin = queue.popleft()

        if subin == k:
            cnt += 1
        
        for i in [ subin*2 , subin + 1, subin - 1]:
            if 0 <= i < max_size:
                if check[i] == -1 or check[i] >= check[subin]+1:
                    check[i] = check[subin] + 1
                    queue.append(i)


bfs()

print(check[k])
print(cnt)
