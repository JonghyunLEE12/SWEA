a = int(input())

if a == 1:
    print(a, 'is odd')
elif a & 2 == 0:
    print(a,'is even')
else:
    print(a, 'is odd')