#푸는중
N = int(input())
numbers = input()

result = 0
if numbers[1] == '+':
    result += int(numbers[0]) + int(numbers[2])
elif numbers[1] == '-':
    result += int(numbers[0]) + int(numbers[2])
elif numbers[1] == '*':
    result += int(numbers[0]) + int(numbers[2])

# print(result)

for i in range(3,N):
    if i % 2:
        if numbers[i] == '+':
            result = result + int(numbers[i+1])
        elif numbers[i] == '-':
            result = result - int(numbers[i+1])
        elif numbers[i] == '*':
            result = result * int(numbers[i+1])
    else:
        continue
print(result)


# for i in range(1,N):
#     #i의 첫번수가 홀수인 경우 0 , 2 , 4, 6 ==> 번호가 저장되어 있음
#     if i % 2:
#         if numbers[i] == '+':
#             result += int(numbers[i-1]) + int(numbers[i+1])
#         elif numbers[i] == '-':
#             result += int(numbers[i-1]) + int(numbers[i+1])
#         elif numbers[i] == '*':
#             result += int(numbers[i-1]) + int(numbers[i+1])
#     else:
#         continue
# print(result)