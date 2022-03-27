notes = list(map(int,input().split()))
ascending = [ i for i in range(1,9)]
descending = ascending[::-1]

if notes == ascending:
    print('ascending')
elif notes == descending:
    print('descending')
else:
    print('mixed')