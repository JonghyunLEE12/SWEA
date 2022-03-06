# holes = [[0,0],[127,0],[254,0],[127,254],[0,127],[0,254]]

import math



def find_hole(WB,Target,holes):
    max_degree = 0
    rlt_hole = []
    for hole in holes:
        x = abs(hole[0]-WB[0])
        y = abs(hole[1]-WB[1])
        r = math.sqrt(x**2 + y**2)
        
        setha = ((x**2 + y**2) - (r**2)) / 2*x*y
        setha = math.degrees(setha)
        if setha > max_degree:
            max_degree = setha
            if not rlt_hole :
                rlt_hole.append(hole)
            else :
                rlt_hole.pop()
                rlt_hole.append(hole)
    
    return rlt_hole

def find_setha():
    x = abs(hole[0] - WB[0])
    y = abs(hole[1] - WB[1])
    a = math.sqrt((x**2) + (y**2) )
    r = 5.73
    radian = math.atan(y/x)
    setha1 = math.degrees(radian)
    # print(setha1)
    
    x2 = abs(Target[0] - WB[0])
    y2 = abs(Target[1] - WB[1])
    
    c = math.sqrt(x2**2 + y2**2)
    
    x3 = abs(hole[0]-Target[1])
    y3 = abs(hole[1]-Target[1])
    
    b = math.sqrt(x3**2 + y3**2)
    
    cosC = (a**2 + b**2 - c**2) / 2*a*b
    cosC = math.cos(cosC)
    # print(cosC) -> 0.4277944587747991 
    
    d =  ((a * ( 1 - cosC))**2 + b+(2*r) - (a*cosC)**2) ** 0.5
    # print(d) -> 76.96748667016924 
    
    cos_setha2 = (a**2)+(d**2)-((b+2*a)**2) / 2 *( a*d )
    cos_setha2 = math.cos(cos_setha2)
    setha2 = math.degrees(cos_setha2)
    # print(setha2)
    
    # print(setha1 , setha2)
    rlt = setha1 + setha2
    print(rlt)
    return
    

WB = [65,65]
Target = [180,65]
holes = [[0,0],[127,0],[254,0],[127,254],[0,127],[0,254]]


# hole = [254,127]

hole = find_hole(WB,Target,holes)[0]
print(hole)
find_setha()