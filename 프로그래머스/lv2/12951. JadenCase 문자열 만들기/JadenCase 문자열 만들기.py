# def solution(s):
#     answer = ''
#     words = s.split(" ")
#     for w in words:
#         if w == " ":
#             answer += " "
#             continue
#         if w.isalpha():
#             answer += w.title() + " "
#         else:
#             answer += w+ " "
#     return answer[:-1]


def solution(s):
    answer = ''
    
    s=s.split(" ")#자르고
    
    for i in s:
        if i=="":# 공백도 출력해줘야함... 생략 ㄴㄴ
            answer+=" "
            continue
        
        memo=""
        i=i.lower()# 모두 소문자로!
        
        if ord(i[0])>=48 and ord(i[0])<=57:# 첫글자가 숫자일시 
            answer+=i+" "
            continue
        else:# 첫글자가 문자일시 첫글자 대문자로
            memo=i[0]
            memo=memo.upper()
            i=memo+i[1:]
            answer+=i+" "
    
    
    return answer[:-1]