T = int(input())

def find(target):
    if parents[target] == target:
        return target
    else:
        y = find(parents[target])
        parents[target] = y
        return y 


def union(a,b):
    a = find(a)
    b = find(b)

    if parents[a] != b:
        parents[a] = b
        number[b] += number[a]
    
    print(number[b])

for tc in range(T):
    f = int(input())

    parents, number = {},{}
    for i in range(f):
        a,b = input().split(' ')
        if a not in parents:
            parents[a] = a
            number[a] = 1
        
        if b not in parents:
            parents[b] = b
            number[b] = 1

        union(a,b)