from collections import deque


n,k = map(int,input().split(' '))
max_value = 100001

check = [-1] * max_value
check[n] = 0

queue = deque()
queue.append(n)
cnt = 0

while queue:
    subin = queue.popleft()

    if subin == k:
        print(check[subin])
        break

    
    if 0 <= subin-1 < max_value and check[subin-1] == -1:
        check[subin-1] = check[subin] + 1
        queue.append(subin-1)
    
    if 0 <= subin * 2 < max_value and check[subin*2] == -1:
        check[subin*2] = check[subin]
        queue.appendleft(subin*2)
    
    if 0 <= subin+1 < max_value and check[subin+1] == -1:
        check[subin+1] = check[subin] + 1
        queue.append(subin+1)