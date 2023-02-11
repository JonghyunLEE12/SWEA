# def solution(files):
#     answer = []
    
#     def divide(fi):
#         divFi = []
#         head = ''
#         number = ''
#         tail = ''
        
#         for i in range(len(fi)):
#             if fi[i].isdigit() == False:
#                 if len(number) == 0:
#                     head += fi[i]
#                 else:
#                     tail += fi[i]
#             else:
#                 number += fi[i]
#         divFi = [head,number,tail]
#         return divFi
    
#     for fi in files:
#         fi = divide(fi)
#         answer.append(fi)
    
#     answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
#     return [ ''.join(x) for x in answer ]




def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(f)): # 문자열 자르기
            if f[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
                number += f[i]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전까지는 HEAD
                head += f[i]
            else:               # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL
                tail = f[i:]
                break
        answer.append((head, number, tail))  # HEAD, NUMBER, TAIL 하나의 튜플로 저장

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  # HEAD 우선, NUMBER 차선으로 정렬

    return [''.join(t) for t in answer]   # 원래 형태로 문자열 만들어서 반환