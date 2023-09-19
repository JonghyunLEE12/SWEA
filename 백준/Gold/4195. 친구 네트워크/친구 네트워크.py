'''
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
'''

tc = int(input())

def find(t):
    if parents[t] == t:
        return t
    else:
        y = find(parents[t])
        parents[t] = y
        return y


def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[a] = b
        number[b] += number[a]
    
    print(number[b])

for _ in range(tc):
    n = int(input())
    
    parents , number = {} , {}

    for i in range(n):
        a,b = input().split(' ')

        if a not in parents:
            parents[a] = a
            number[a] = 1
        
        if b not in parents:
            parents[b] = b
            number[b] = 1

        union(a,b)