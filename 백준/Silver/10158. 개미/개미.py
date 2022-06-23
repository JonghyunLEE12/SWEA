def ant():
    # x = (p+t)%w y=(q+t)%h
    global p,q,t
    a = (p+t) // w
    b = (q+t) // h
    if a % 2 == 0:
        x = (p+t) % w
    else:
        x = w - (p+t) % w
    if b % 2 == 0:
        y =(q+t) % h
    else:
        y = h - (q + t) % h
    return x,y

w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())
rlt = ant()
print(*rlt)