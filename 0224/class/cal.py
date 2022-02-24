operation = '(6+5*(2-8)/2)'
stack = []
rlt = []

# 1. 중위 표현식을 순회
for token in operation:
    # 2. 만약에, 너 숫자면 결과에 push
    if token.isdigit():
        rlt.append(token)
    else:       # 연산자 라면?
        if not stack:           # 스택이 비어 있다면
            stack.append(token)
        else : # 스택이 비어 있지 않다면 (icp,isp 비교 후 push )
            if token == '(':
                stack.append(token)
            elif token == ')':
                temp = stack.pop()
                while temp != '(':    # 닫는 괄호 일 때, 여는 괄호를 만날 때 까지, top 에 있는 내용을 저장
                    rlt.append(temp)
                    temp = stack.pop()
            # icp == 2
            elif token == '*' or token == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    rlt.append(stack.pop())
                stack.append(token)

            # icp == 1
            elif token == '+' or token == '-':
                while stack and stack[-1] != '(':                # 위에서 다 걸러졌기 때문에 icp가 2 일때처럼 안해도 된다.
                    rlt.append(stack.pop())
                stack.append(token)

# stack에 남아있다면,모두 꺼내서 push
for _ in range(len(stack)):
    rlt.append(stack.pop())

print(rlt)



# 후위 표현식 계산 하기
# 숫자면, stack의 push
# 연산자를 만나면, num1,num2 pop() 후 계산 한 뒤 push
stack2 = []
for i in rlt:
    if i.isdigit():
        stack2.append(int(i))
    else:
        # 연산할때는, 맨 처음 pop 해준것이 뒤로 가게 됨
        num2 = stack2.pop()
        num1 = stack2.pop()
        if i == '+':
            stack2.append(num1+num2)

        elif i == '*':
            stack2.append(num1*num2)

        elif i == '-':
            stack2.append(num1-num2)

        elif i == '/':
            stack2.append(num1/num2)

ans = stack2.pop()
print(ans)