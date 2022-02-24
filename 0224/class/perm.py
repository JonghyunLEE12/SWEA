# 순서 외우기
def perm(i):
    if i == len(p):
        print(p)
    else:
        for j in range(i,len(p)):
            p[i],p[j] = p[j],p[i] # 순서 바꾸고
            perm(i+1)             # 재귀 호출 하고
            p[i], p[j] = p[j], p[i] # 끝날시 원래대로


p = [1,2,3,4]
perm(0)