# def solution(new_id):
#     answer = ''
    
#     # 1 소문자 치환
#     new_id = new_id.lower()
    
#     # 2 소문자, 숫자 , - , _ , . 를 제외한 모든문자 제거
#     for word in new_id:
#         if word.isalnum() or word in ['-','_','.']:
#             answer += word
#     new_id = answer
    
#     # 3 new_id 에서 마침표가 두번이상 된 부분을 하나로 치환
#     while ".." in new_id:
#         new_id = new_id.replace("..",".")

#     # 4 마침표가 처음이나 끝에 위치한다면 제거하기
#     new_id = list(new_id)
#     if new_id[0] == '.' or new_id[-1] =='.':
#         if new_id[0] == '.' :
#             new_id = new_id[1:]
#         else:
#             new_id.pop()
    
#     # 5 new_id가 빈문자열 이라면 "a"를 대입
#     if len(new_id) == 0:
#         new_id.append('a')
    
#     # 6 len(new_id) 16자 이상이면 new_id 의 첫 15개 문자를 제외한 나머지 문자 제거
#     if len(new_id) >= 16:
#         new_id = new_id[:15]
#         if new_id[-1] == '.':
#             new_id.pop()
    
    
#     # 7 new_id 길이가 2자 이하면 마지막 문자를 길이가 3이 될떄까지 반복해서 붙인다
#     if len(new_id) <= 2:
#         while len(new_id) < 3:
#             new_id.append(new_id[-1])
            
    
    
#     return ''.join(new_id)




import re
def solution(new_id):    
    #1단계 & 2단계 소문자 치환, 제거
    answer = re.sub('[^0-9a-z_.\-]+','',new_id.lower())
    
    #3단계 . 2번 이상을 1개로 압축
    answer = re.sub('\.\.+','.',answer)
    
    #4단계 양끝 . 제거
    answer = answer.strip('.')
    
    #5단계 빈문자열 a 추가
    if answer =='': answer='a'
        
    #6단계 15개제외하고 문자모두제거, 우측 . 제거
    answer = answer[:15].rstrip('.')
        
    #7단계 길이 3 될 때까지 끝 문자 추가    
    answer+=answer[-1]*(3-len(answer))
        
    return answer