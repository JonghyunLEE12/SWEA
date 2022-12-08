n = int(input())

num_list = []
for i in range(n):
    x,y = map(int,input().split(' '))
    num_list.append([x,y])

num_list.sort()
# num_list.sort(key=lambda x : (x[1],x[0]))

# max_height 인덱스
i = 0
result = 0
for num in num_list:
    if num[1] > result:
        result = num[1]
        idx = i
    i += 1


height = num_list[0][1]

# 앞 부터 최대 높이 까지
for i in range(idx):
    if height < num_list[i+1][1]:
        result += height * (num_list[i+1][0] - num_list[i][0])
        height = num_list[i+1][1]
    else:
        result += height * (num_list[i+1][0] - num_list[i][0])

# 뒤에서 부터
height = num_list[-1][1]

for i in range(n-1,idx,-1):
    if height < num_list[i-1][1]:
        result += height * (num_list[i][0] - num_list[i-1][0])
        height = num_list[i-1][1]
    else :
        result += height * (num_list[i][0] - num_list[i-1][0])
print(result)

