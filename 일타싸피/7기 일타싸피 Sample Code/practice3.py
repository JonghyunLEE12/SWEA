import math

def find_hole(holes):
    max_setha = 0
    rlt_hole = []
    for hole in holes:
        x = abs(hole[0] - WB[0])
        y = abs(hole[1] - WB[1])
        r = math.sqrt(x**2 + y**2)

        setha = ((x**2 + y**2) - (r**2)) / 2*x*y
        setha = math.degrees(setha)
        if setha > max_setha:
            max_setha = setha
            if not rlt_hole:
                rlt_hole.append(hole)
            else:
                rlt_hole.pop()
                rlt_hole.append(hole)
    return rlt_hole


def find_setha(hole):
    hole = sum(hole,[])
    # a 구하기
    x = abs(hole[0] - WB[0])
    y = abs(hole[1] - WB[1])

    a = math.sqrt(x**2 + y**2)
    
    # setha1 구하기
    radian = math.atan(y/x)
    setha1 = math.degrees(radian)

    # c 구하기
    x2 = abs(Target[0] - WB[0])
    y2 = abs(Target[1] - WB[1])

    c = math.sqrt(x2**2 + y2**2)

    # b 구하기
    x3 = abs(Target[0] - hole[0])
    y3 = abs(Target[1] - hole[1])

    b = math.sqrt(x3**2 + y3**2)

    # cosC 구하기
    cosC = ((a**2 + b**2) - c**2)  / 2*a*b
    cosC = math.cos(cosC)
    print(cosC)


    # d 구하기 피타고라스!
    d = ((a*(1-cosC))**2 + ((b+2*r) - (a*cosC))**2)**0.5
    print(d)

    # setha2 구하기
    cos_setha2 = (a**2 + d**2) - (b+2*r)**2 / 2*a*d
    setha2 = math.cos(cos_setha2)
    
    return  setha1 + setha2


WB = [65,65]
Target = [180,65]
holes = [[0,0],[127,0],[254,0],[127,254],[0,127],[0,254]]
r = 5.73

hole = find_hole(holes)
angle = find_setha(hole)
print(angle)