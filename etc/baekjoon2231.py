#분해합
# N = int(input())
# N = 245
# total = N
# for i in str(N):
#     total += int(i)
# # print(total) => 245의 분해합 : 256

#생성자 -> 분해합의 역순
N = 256
minus = N
for i in str(N):
    minus -= int(i)
print(minus)