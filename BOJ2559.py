# import sys

# N,K = map(int,sys.stdin.readline().split())
# temps = list(map(int,sys.stdin.readline().split()))

# rlt = []

# for i in range(N):
#     if i+K > N:
#         break
#     result=temps[i]
#     for j in range(i+1,i+K):
#         result += temps[j]
#     rlt.append(result)

# print(max(rlt))



# N,K = map(int,input().split())
# temps = list(map(int,input().split()))

# rlt = []
# for i in range(N):
#     if i+K > N:
#         break
#     result=temps[i]
#     for j in range(i+1,i+K):
#         result += temps[j]
#     rlt.append(result)    

# print(max(rlt))



# N,K = map(int,input().split())
# temps = list(map(int,input().split()))

# max_num = -9999
# for i in range(N):
#     if i+K > N:
#         break
#     result=temps[i]
#     for j in range(i+1,i+K):
#         result += temps[j]

#     if result > max_num:
#         max_num= result
    
# print(max_num)




N,K = map(int,input().split())
temps = list(map(int,input().split()))


sum_num = sum(temps[:K])
max = sum_num
for i in range(N-K):
    sum_num -= temps[i]
    sum_num += temps[i+K]

    if sum_num > max:
        max=sum_num
print(max)



