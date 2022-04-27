n,m = map(int,input().split())
numbers = list(map(int,input().split()))
# 증가하는 순으로 출력 : sort()
numbers.sort()

# 값을 담아줄 리스트
rlt = []

def dfs(idx):
    global rlt
    # 가지치기
    if len(rlt) == m:
        print(*rlt)
    for i in range(idx,n):
        if numbers[i] not in rlt:
            rlt.append(numbers[i])
            dfs(i+1)
            rlt.pop()


dfs(0)