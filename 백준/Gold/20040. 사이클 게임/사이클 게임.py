
n,m = map(int,input().split(' '))
parents = [ i for i in range(n+1)]
gameover = 0


def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y




def union(a,b,idx):
    global gameover
    a = find(a)
    b = find(b)

    if a != b:
        parents[max(a,b)] = min(a,b)
    elif gameover == 0:
        gameover = idx

for i in range(m):
    h,v = map(int,input().split(' '))
    union(h,v,i+1)


print(gameover)