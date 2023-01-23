# def solution(today, terms, privacies):
#     answer = []
    
    
#     terms_dict = {}
    
#     for te in terms:
#         te = list(te.split(' '))
#         terms_dict[te[0]] = te[1]
        
#     def check_terms(pri):
        
#         addMonth = terms_dict[pri[1]]

#         date = list(pri[0].split('.'))
        
#         date[1] = str(int(date[1]) + int(addMonth)) 
#         if int(date[1]) > 12:
#             date[1] = '0'+str(int(date[1])-12)
#             date[0] = str(int(date[0])+1)
        
        
 
#         todayCheck = list(today.split('.'))
    
        
#         if int(date[0]) > int(todayCheck[0]):
#             return True
#         else:
#             if int(date[1]) > int(todayCheck[1]):
#                 return True
#             else:
#                 if int(date[2]) > int(todayCheck[2]):
#                     return True
        
#         return False
    
#     for pri in privacies:
#         pri = list(pri.split(' '))
#         if check_terms(pri):
#             print(pri)
#     return answer



from datetime import date
def solution(today, terms, privacies):
    answer = []
    mon = {}
    today_time = date(int(today[:4]), int(today[5:7]),int(today[8:10]))

    for sep in terms:
        ter, mont = sep.split(' ') # term의 값들을 띄어쓰기로 분리 후 ter, mont 에 저장
        mon[ter] = mont # 딕셔너리에 키, 값으로 저장
    
    for j,i in enumerate(privacies,1):
        dateday, term = i.split(' ')
        year = int(dateday[:4])

        month = int(dateday[5:7]) + int(mon[term])  # 수집된 정보의 달 + 해당 유효기간
        monthPer = int(month / 12) # 전체 달이 12이므로 12로 나눈 몫을 구하여 년도에 더해줌
        year = year + monthPer 
        if int(dateday[8:10]) == 1: # 수집된 정보의 일이 01이라면
            if month % 12 == 0: 
                month = month % 12 -1 
                year -=1
            else:
                month = month % 12 -1
        else:
            month = month % 12

        if month == 0:
            month = 12
            year -=1
        elif month < 0:
            month = 12 + month

        day = dateday[8:10]
        if  day == '01': 
            day = 28
            
        else:
            day = int(day) - 1
        
        old_time = date(year,month,day)
        if today_time > old_time:
            answer.append(j)

    return answer