import math

# 가장 가까운 구멍 찾기

def find_hole(holes):
    max_hole = 0
    rlt_hole = []
    for hole in holes:
        x = abs(hole[0] - WB[0])
        y = abs(hole[1] - WB[1])
        r = math.sqrt(x**2 + y**2)
        
        setha = ((x**2 + y**2) - r**2 ) / (2*x*y)
        setha = math.degrees(setha)
        if setha > max_hole:
            max_hole = setha
            if not rlt_hole:
                rlt_hole.append(hole)
            else:
                rlt_hole.pop()
                rlt_hole.append(hole)
    return rlt_hole

# 각도 구하기

def find_setha(hole):
    hole = sum(hole,[])
    x = abs(hole[0] - WB[0])
    y = abs(hole[1] - WB[1])
    a = math.sqrt(x**2 + y**2)
    radian = math.atan(y/x)
    setha1 = math.degrees(radian)
    
    x2 = abs(Target[0] - WB[0])
    y2 = abs(Target[1] - WB[1])

    c = math.sqrt(x2**2 + y2**2)

    x3 = abs(hole[0] - Target[0])
    y3 = abs(hole[1] - Target[1])

    b = math.sqrt(x3**2 + y3**2)

    # a, b, c 이용하여 cosC 구할 수 있음
    cosC = ((a**2 + b**2) - c**2) / 2*a*b
    cosC = math.cos(cosC)
    print(cosC)
    # 이제 d를 구하자
    d = ((a*(1-cosC))**2 + ((b+2*r)-(a*cosC))**2)**0.5


    # setha2 구하기
    cos_setha2 = (a**2) + (d**2) - (b+2*r)**2 / 2*a*d
    cos_setha2 = math.cos(cos_setha2)
    setha2 = math.degrees(cos_setha2)

    # 결과
    rlt = setha1 + setha2
    print(rlt)
    return

WB = [65,65]
Target = [180,65]
holes = [[0,0],[127,0],[254,0],[127,254],[0,127],[0,254]]
r = 5.73

hole = find_hole(holes)
angle = find_setha(hole)
