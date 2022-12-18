N,K = map(int,input().split())
temp_arr = list(map(int,input().split()))



sum_num = sum(temp_arr[:K])
max_num = sum_num

for i in range(len(temp_arr)-K):
    sum_num -= temp_arr[i]
    sum_num += temp_arr[i+K]

    if max_num < sum_num:
        max_num = sum_num

print(max_num)
