'''
4
3
4
1
1
'''

g = int(input())
p = int(input())

parents = [ x for x in range(g+1)]
plane = []
count = 0

for _ in range(p):
    plane.append(int(input()))


def find(target):
    if target == parents[target]:
        return target
    
    else:
        y = find(parents[target])
        parents[target] = y
        return y



def union(a,b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parents[a] = b


for pl in plane:
    x = find(parents[pl])

    if x == 0:
        break

    union(x,x-1)
    count += 1

print(count)

