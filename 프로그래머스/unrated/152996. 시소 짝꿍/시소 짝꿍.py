# def solution(weights):
#     answer = 0
#     #1m, 2m, 3m , 4m
#     n = len(weights)
    
#     def check(num1,num2):
#         if num1 == num2 :
#             return True
#         else:
#             if 
        
        
#     for i in range(n):
#         for j in range(i,n):
#             if i == j:
#                 continue
#             if check(weights[i],weights[j]):
#                 answer += 1
#     return answer

def solution(weights):
    answer = 0
    answerdiv2 = 0
    dic = {}

    for i in weights:
        dic[i] = dic.get(i, 0)
        dic[i] += 1


    for i in dic:
        x2 = i * 2
        if(x2 % 3 == 0):
            if(int(x2 / 3) in dic):
                answerdiv2 += int(dic[i] * dic[x2 / 3])
        if(x2 % 4 == 0):
            if(int(x2 / 4) in dic):
                answerdiv2 += int(dic[i] * dic[x2 / 4])

        x3 = i * 3
        if(x3 % 2 == 0):
            if(int(x3 / 2) in dic):
                answerdiv2 += int(dic[i] * dic[x3 / 2])
        if(x3 % 4 == 0):
            if(int(x3 / 4) in dic):
                answerdiv2 += int(dic[i] * dic[x3 / 4])

        x4 = i * 4
        if(x4 % 2 == 0):
            if(int(x4 / 2) in dic):
                answerdiv2 += int(dic[i] * dic[x4 / 2])
        if(x4 % 3 == 0):
            if(int(x4 / 3) in dic):
                answerdiv2 += int(dic[i] * dic[x4 / 3])

        answer += int(dic[i] * (dic[i] - 1) / 2)

    answer += int(answerdiv2/2)


    return answer