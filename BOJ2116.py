N = int(input())
dices = []
for i in range(N):
    dices.append(list(map(int,input().split())))

max_num = 0

# 주사위 아랫면에 따른 윗면 로테이트
rotate = {
    0 : 5,
    1 : 3,
    2 : 4,
    3 : 1,
    4 : 2,
    5 : 0
}

for i in range(6):
    result = []
    temp = [1, 2, 3, 4, 5, 6]
    temp.remove(dices[0][i])
    next = dices[0][rotate[i]]
    temp.remove(next)
    result.append(max(temp))

    for j in range(1,N):
        temp = [1, 2, 3, 4, 5, 6]
        temp.remove(next)
        next = dices[j][rotate[dices[j].index(next)]]
        temp.remove(next)
        result.append(max(temp))
    result = sum(result)
    if max_num < result:
        max_num = result

print(max_num)