
N = int(input())

#number 변수에 N을 저장
number = N
#cnt 변수 선언
cnt = 0
while True:
    #26
    # a 값에 number를 10으로 나눈 몫을 저장
    a = number //10 #2
    # b 값에 number의 10으로 나눈 나머지 저장
    b = number % 10  #6
    # c 값에 number의 10의 자리수와 1의 자리수를 저장후 10으로 나눈 나머지값 저장
    c = (a+b) % 10 #8
    # number에 새로운 값을 대입
    number = (b*10) + c #68
    cnt += 1
    # number 의 값과 N의 값이 똑같을 때, while문을 빠져나옴
    if number == N:
        break
print(cnt)