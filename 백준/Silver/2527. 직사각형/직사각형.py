# 단 항상 x<p, y<q
for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    # case d
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')
        continue
    # case c
    elif x1==p2 or x2==p1:
        if q1==y2 or q2==y1:
            print('c')
            continue
        # case b
        else:
            print('b')
            continue
    # case b
    elif q1==y2 or q2==y1:
            print('b')
            continue
    # case a
    else:
        print('a')
        continue