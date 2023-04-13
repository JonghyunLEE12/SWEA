N = int(input())
nums = list(map(int, input().split())) # N개의 숫자를 저장

sum_nums = sum(nums) # 먼저 숫자를 다 더한다.
res = 0

for n in nums: # 이제 숫자를 하나씩 빼오면서 위의 2,3,4번을 반복한다.
    sum_nums -= n
    res += sum_nums * n

print(res)