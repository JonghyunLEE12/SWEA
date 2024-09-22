n,k = map(int,input().split(' '))
stuff = [[0,0]]
napSack = [ [0 for _ in range(k+1)]for _ in range(n+1)]


for _ in range(n):
    stuff.append(list(map(int,input().split(' '))))

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            napSack[i][j] = napSack[i-1][j]
        else:
            napSack[i][j] = max(value + napSack[i-1][j-weight], napSack[i-1][j])


print(napSack[n][k])