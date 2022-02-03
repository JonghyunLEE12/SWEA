
# 단 항상 x<p, y<q
for _ in range(4):
    '''
    직사각형 1 : (x1, y1) , (p1,q1)
    직사각형 2 : (x2, y2) , (p2,q2)
    '''
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    # case d 교차하지 않음
    if p1 < x2 or p2 < x1 or q2<y1 or q1 < y2:
        print('d')
        continue
    # case c
    # 점으로 일치 하는 경우
    elif x1==p2 or x2==p1:
        if q1==y2 or q2==y1:
            print('c')
            continue
        # case b
        else:
            print('b')
            continue
    # case b
    # 선이 맞닿은 경우
    elif q1==y2 or q2==y1:
            print('b')
            continue
    # case a
    else:
        print('a')
        continue


