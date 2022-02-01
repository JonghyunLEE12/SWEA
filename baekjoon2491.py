# N = int(input())
# numbers = list(map(int,input().split()))
#
# cnt = 1
# max_cnt = 1
# for i in range(len(numbers)-1):
#     if numbers[i] <= numbers[i+1]:
#         cnt += 1
#     else :
#         cnt = 1
#     if max_cnt < cnt:
#         max_cnt = cnt
#
# for i in range(len(numbers)-1):
#     if numbers[i] >= numbers[i+1]:
#         cnt += 1
#     else :
#         cnt = 1
#     if max_cnt < cnt:
#         max_cnt = cnt
# print(max_cnt)





N = int(input())
numbers = list(map(int,input().split()))

cnt = 1
max_cnt = 1

#증가 할 때
for i in range(N-1):
    if numbers[i] <= numbers[i+1]:
        cnt +=1
    else:
        cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt
#감소 할 떄
for i in range(N-1):
    if numbers[i] >= numbers[i+1]:
        cnt += 1
    else:
        cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)
